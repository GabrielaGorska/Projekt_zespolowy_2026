from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from typing import List

from database import models, connections, schemas
from utils.config import settings

router = APIRouter(prefix="/admin", tags=["Admin Management"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_admin(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(connections.get_db),
):
    """Dependency that checks if the current user is an admin based on the JWT token.
    Raises 401 if token is invalid, 403 if user is not an admin."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the JWT token to get user information
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")

        if email is None or role is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    # check if role is admin
    if role != models.UserRole.ADMIN.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have enough permissions to access this resource"
        )

    # fetch user from database to ensure they still exist and are active
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception

    return user


@router.patch("/promote/{user_id}", response_model=schemas.UserOut)
def promote_to_admin(user_id: int,
                     db: Session = Depends(connections.get_db),
                     current_admin: models.User = Depends(get_current_admin)):
    """Promotes a user to an administrator role.
    Only for existing users. Admin accounts are auto-approved."""
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = models.UserRole.ADMIN
    user.is_approved = True  # Ensure admin accounts are approved

    db.commit()
    db.refresh(user)
    return user


@router.get("/users", response_model=List[schemas.UserOut])
def get_all_users(db: Session = Depends(connections.get_db),
                  current_admin: models.User = Depends(get_current_admin)):
    """
    Returns a list of all users in the system.
    Only for administrators.
    """
    users = db.query(models.User).all()
    return users
