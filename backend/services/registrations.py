"""Sign-up, cancel, confirm-by-token, and related email notifications."""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import (
    Event,
    EventRegistration,
    EventStatus,
    RegistrationStatus,
    User,
)
from database.schemas import RegistrationOut
from services import email as email_service
from services.events import count_taken_slots, ensure_event_open
from utils.tokens import generate_token


def registration_to_out(reg: EventRegistration, event: Event | None, user: User | None) -> RegistrationOut:
    name = None
    if user and user.first_name:
        name = f"{user.first_name} {user.last_name or ''}".strip()
    return RegistrationOut(
        id=reg.id,
        event_id=reg.event_id,
        event_title=event.title if event else None,
        user_id=reg.user_id,
        volunteer_name=name,
        volunteer_email=user.email if user else None,
        status=reg.status,
        registered_at=reg.registered_at,
    )


def create_registration(db: Session, event: Event, volunteer: User) -> EventRegistration:
    ensure_event_open(event)

    existing = (
        db.query(EventRegistration)
        .filter(
            EventRegistration.event_id == event.id,
            EventRegistration.user_id == volunteer.id,
        )
        .first()
    )
    if existing:
        # Re-activate after cancel if slots still available
        if existing.status == RegistrationStatus.CANCELLED:
            if count_taken_slots(db, event.id) >= event.max_slots:
                raise HTTPException(status_code=400, detail="No free slots available")
            existing.status = RegistrationStatus.PENDING
            existing.confirmation_token = generate_token()
            db.commit()
            db.refresh(existing)
            _notify_signup(db, event, volunteer, existing.confirmation_token)
            return existing
        raise HTTPException(status_code=400, detail="Already registered for this event")

    if count_taken_slots(db, event.id) >= event.max_slots:
        raise HTTPException(status_code=400, detail="No free slots available")

    token = generate_token()
    reg = EventRegistration(
        event_id=event.id,
        user_id=volunteer.id,
        status=RegistrationStatus.PENDING,
        confirmation_token=token,
    )
    db.add(reg)
    db.commit()
    db.refresh(reg)
    _notify_signup(db, event, volunteer, token)
    return reg


def cancel_registration(db: Session, reg: EventRegistration, event: Event) -> EventRegistration:
    if reg.status == RegistrationStatus.CANCELLED:
        raise HTTPException(status_code=400, detail="Registration already cancelled")
    reg.status = RegistrationStatus.CANCELLED
    reg.confirmation_token = None
    db.commit()
    db.refresh(reg)
    volunteer = db.query(User).filter(User.id == reg.user_id).first()
    if volunteer:
        email_service.send_registration_cancelled_email(volunteer.email, event.title)
    return reg


def confirm_by_token(db: Session, token: str) -> EventRegistration:
    reg = (
        db.query(EventRegistration)
        .filter(EventRegistration.confirmation_token == token)
        .first()
    )
    if not reg:
        raise HTTPException(status_code=400, detail="Invalid or expired confirmation link")
    if reg.status == RegistrationStatus.CONFIRMED:
        return reg
    if reg.status == RegistrationStatus.CANCELLED:
        raise HTTPException(status_code=400, detail="Registration was cancelled")

    reg.status = RegistrationStatus.CONFIRMED
    reg.confirmation_token = None
    db.commit()
    db.refresh(reg)
    return reg


def _notify_signup(db: Session, event: Event, volunteer: User, token: str):
    email_service.send_registration_confirm_email(
        volunteer.email, token, event.title
    )
    org = db.query(User).filter(User.id == event.organization_id).first()
    if org:
        name = f"{volunteer.first_name or ''} {volunteer.last_name or ''}".strip() or volunteer.email
        email_service.send_new_signup_notify_organizer(org.email, event.title, name)
