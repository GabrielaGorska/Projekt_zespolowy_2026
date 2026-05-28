"""FastAPI dependencies: JWT auth, role checks, event ownership."""

from typing import Callable

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from database.connections import get_db
from database.models import User, UserRole
from utils.config import settings

# Swagger "Authorize" uses this path; must match routers/auth login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def _decode_token(token: str) -> dict:
    """Validate JWT signature and expiry; raises 401 on failure."""
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Resolve Bearer token to DB user (any role)."""
    payload = _decode_token(token)
    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


def get_current_active_user(user: User = Depends(get_current_user)) -> User:
    """Reject blocked accounts (is_active=False)."""
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is blocked")
    return user


def require_roles(*roles: UserRole) -> Callable:
    """Factory: dependency that allows only given roles."""
    allowed = {r.value for r in roles}

    def _checker(user: User = Depends(get_current_active_user)) -> User:
        if user.role.value not in allowed:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user

    return _checker


def get_current_admin(user: User = Depends(require_roles(UserRole.ADMIN))) -> User:
    return user


def get_current_organization(user: User = Depends(require_roles(UserRole.ORGANIZATION))) -> User:
    """Approved org only — required to create/manage events."""
    if not user.is_approved:
        raise HTTPException(status_code=403, detail="Organization account pending approval")
    return user


def get_current_volunteer(user: User = Depends(require_roles(UserRole.VOLUNTEER))) -> User:
    return user


def ensure_event_owner(event_org_id: int, user: User):
    """Org may touch only own events; admin may touch all."""
    if user.role == UserRole.ADMIN:
        return
    if user.role != UserRole.ORGANIZATION or event_org_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed to manage this event")
