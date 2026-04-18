from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import models, schemas, connections
from utils import auth



router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register/volunteer", response_model=schemas.UserOut)
def register_volunteer(user_data: schemas.VolunteerCreate, db: Session = Depends(connections.get_db)):
    # Check if email exists
    if db.query(models.User).filter(models.User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        email=user_data.email,
        hashed_password=auth.hash_password(user_data.password),
        role=models.UserRole.VOLUNTEER,
        is_active=True,
        is_approved=True  # Volunteers are auto-approved
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/register/organization", response_model=schemas.UserOut)
def register_organization(user_data: schemas.OrganizationCreate, db: Session = Depends(connections.get_db)):
    if db.query(models.User).filter(models.User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        email=user_data.email,
        hashed_password=auth.hash_password(user_data.password),
        role=models.UserRole.ORGANIZATION,
        is_active=True,
        is_approved=False  # Requires Admin approval (Spec point 3.1)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(connections.get_db)
):
    """Authenticate user and return JWT token if valid."""
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"sub": user.email, "role": user.role.value})
    return {"access_token": access_token, "token_type": "bearer"}
