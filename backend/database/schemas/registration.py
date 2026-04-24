"""Event registration API shapes (participant list, email confirm token)."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from database.models import RegistrationStatus


class RegistrationOut(BaseModel):
    id: int
    event_id: int
    event_title: Optional[str] = None
    user_id: int
    volunteer_name: Optional[str] = None
    volunteer_email: Optional[str] = None
    status: RegistrationStatus
    registered_at: datetime

    model_config = {"from_attributes": True}


class RegistrationConfirm(BaseModel):
    token: str
