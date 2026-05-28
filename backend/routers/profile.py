"""Logged-in user profile updates."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import schemas
from database.connections import get_db
from database.models import User
from utils.dependencies import get_current_active_user

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.patch("/me", response_model=schemas.UserOut)
def update_profile(
    data: schemas.UserProfileUpdate,
    user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user
