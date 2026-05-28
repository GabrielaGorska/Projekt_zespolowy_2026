"""Event create/update/list/detail payloads and validation rules."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationInfo, field_validator

from database.models import EventStatus


class EventBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1, max_length=500)
    start_date: datetime
    end_date: Optional[datetime] = None
    max_slots: int = Field(..., gt=0)
    category: Optional[str] = None

    @field_validator("end_date")
    @classmethod
    def end_not_before_start(cls, end_date: Optional[datetime], info: ValidationInfo):
        start = info.data.get("start_date")
        if end_date and start and end_date < start:
            raise ValueError("end_date cannot be before start_date")
        return end_date


class EventCreate(EventBase):
    pass


class EventUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    max_slots: Optional[int] = Field(None, gt=0)
    category: Optional[str] = None
    status: Optional[EventStatus] = None


class EventOut(EventBase):
    id: int
    organization_id: int
    organization_name: Optional[str] = None
    status: EventStatus
    created_at: datetime
    taken_slots: int = 0
    free_slots: int = 0

    model_config = {"from_attributes": True}


class EventListOut(BaseModel):
    id: int
    title: str
    location: str
    start_date: datetime
    organization_name: Optional[str] = None
    status: EventStatus
    max_slots: int
    taken_slots: int
    free_slots: int

    model_config = {"from_attributes": True}
