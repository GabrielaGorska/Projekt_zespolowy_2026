import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database.connections import Base


class EventStatus(enum.Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    CANCELLED = "cancelled"


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(500), nullable=False)
    category = Column(String(100), nullable=True)

    start_date = Column(DateTime, nullable=False, index=True)
    end_date = Column(DateTime, nullable=True)

    max_slots = Column(Integer, nullable=False)
    status = Column(Enum(EventStatus), default=EventStatus.ACTIVE, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    organization = relationship("User", backref="events")
    registrations = relationship("EventRegistration", back_populates="event")
