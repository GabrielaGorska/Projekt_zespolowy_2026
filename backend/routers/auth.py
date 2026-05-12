"""Authentication: register, login, JWT, forgot/reset password."""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import schemas
from database.connections import get_db
from database.models import PasswordResetToken, User, UserRole
from services import email as email_service
from utils import auth as auth_utils
from utils.config import settings
from utils.dependencies import get_current_active_user
from utils.tokens import expiry_from_minutes, generate_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register/volunteer", response_model=schemas.UserOut)
def register_volunteer(data: schemas.VolunteerCreate, db: Session = Depends(get_db)):
    """Create volunteer — auto-approved, can log in immediately."""
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=data.email,
        hashed_password=auth_utils.hash_password(data.password),
        role=UserRole.VOLUNTEER,
        first_name=data.first_name,
        last_name=data.last_name,
        is_active=True,
        is_approved=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/register/organization", response_model=schemas.UserOut)
def register_organization(data: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    """Create org — is_approved=False until admin approves."""
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.nip == data.nip).first():
        raise HTTPException(status_code=400, detail="Organization with this NIP already exists")

    user = User(
        email=data.email,
        hashed_password=auth_utils.hash_password(data.password),
        role=UserRole.ORGANIZATION,
        organization_name=data.organization_name,
        nip=data.nip,
        address=data.address,
        contact_person=data.contact_person,
        phone=data.phone,
        is_active=True,
        is_approved=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=schemas.TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """OAuth2 form uses `username` field for email."""
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not auth_utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is blocked")

    if user.role == UserRole.ORGANIZATION and not user.is_approved:
        raise HTTPException(status_code=403, detail="Organization account pending approval")

    token = auth_utils.create_access_token(
        data={"sub": user.email, "role": user.role.value}
    )
    return schemas.TokenResponse(access_token=token)


@router.get("/me", response_model=schemas.UserOut)
def get_me(user: User = Depends(get_current_active_user)):
    return user


@router.post("/forgot-password", response_model=schemas.MessageResponse)
def forgot_password(body: schemas.ForgotPasswordRequest, db: Session = Depends(get_db)):
    """Always returns same message — do not reveal whether email exists."""
    user = db.query(User).filter(User.email == body.email).first()
    if user:
        token = generate_token()
        db.add(
            PasswordResetToken(
                user_id=user.id,
                token=token,
                expires_at=expiry_from_minutes(settings.RESET_TOKEN_EXPIRE_MINUTES),
            )
        )
        db.commit()
        email_service.send_password_reset_email(user.email, token)
    return schemas.MessageResponse(message="If the email exists, a reset link was sent")


@router.post("/reset-password", response_model=schemas.MessageResponse)
def reset_password(body: schemas.ResetPasswordRequest, db: Session = Depends(get_db)):
    """Consume one-time token from email link."""
    row = (
        db.query(PasswordResetToken)
        .filter(
            PasswordResetToken.token == body.token,
            PasswordResetToken.used_at.is_(None),
        )
        .first()
    )
    if not row or row.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired reset link")

    user = db.query(User).filter(User.id == row.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired reset link")

    user.hashed_password = auth_utils.hash_password(body.new_password)
    row.used_at = datetime.utcnow()
    db.commit()
    return schemas.MessageResponse(message="Password updated successfully")
