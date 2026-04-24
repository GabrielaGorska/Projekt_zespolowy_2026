import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from database.connections import Base


class RegistrationStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class EventRegistration(Base):
    __tablename__ = "event_registrations"
    __table_args__ = (UniqueConstraint("event_id", "user_id", name="uq_event_user"),)

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    status = Column(Enum(RegistrationStatus), default=RegistrationStatus.PENDING, nullable=False)
    registered_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    confirmation_token = Column(String(64), unique=True, nullable=True, index=True)

    event = relationship("Event", back_populates="registrations")
    user = relationship("User", backref="registrations")
