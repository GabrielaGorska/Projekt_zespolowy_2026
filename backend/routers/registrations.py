"""Volunteer sign-up/cancel, participant list, email confirmation endpoint."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import schemas
from database.connections import get_db
from database.models import Event, EventRegistration, RegistrationStatus, User
from services.registrations import (
    cancel_registration,
    confirm_by_token,
    create_registration,
    registration_to_out,
)
from utils.dependencies import (
    ensure_event_owner,
    get_current_active_user,
    get_current_volunteer,
)

router = APIRouter(tags=["Registrations"])


@router.post("/events/{event_id}/register", response_model=schemas.RegistrationOut)
def register_for_event(
    event_id: int,
    volunteer: User = Depends(get_current_volunteer),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    reg = create_registration(db, event, volunteer)
    return registration_to_out(reg, event, volunteer)


@router.delete("/events/{event_id}/register", response_model=schemas.RegistrationOut)
def cancel_event_registration(
    event_id: int,
    volunteer: User = Depends(get_current_volunteer),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    reg = (
        db.query(EventRegistration)
        .filter(
            EventRegistration.event_id == event_id,
            EventRegistration.user_id == volunteer.id,
        )
        .first()
    )
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    reg = cancel_registration(db, reg, event)
    return registration_to_out(reg, event, volunteer)


@router.get("/events/{event_id}/participants", response_model=list[schemas.RegistrationOut])
def list_participants(
    event_id: int,
    user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    ensure_event_owner(event.organization_id, user)

    regs = (
        db.query(EventRegistration)
        .filter(
            EventRegistration.event_id == event_id,
            EventRegistration.status != RegistrationStatus.CANCELLED,
        )
        .all()
    )
    out = []
    for reg in regs:
        vol = db.query(User).filter(User.id == reg.user_id).first()
        out.append(registration_to_out(reg, event, vol))
    return out


@router.get("/registrations/me", response_model=list[schemas.RegistrationOut])
def my_registrations(
    volunteer: User = Depends(get_current_volunteer),
    db: Session = Depends(get_db),
):
    regs = (
        db.query(EventRegistration)
        .filter(
            EventRegistration.user_id == volunteer.id,
            EventRegistration.status != RegistrationStatus.CANCELLED,
        )
        .all()
    )
    result = []
    for reg in regs:
        event = db.query(Event).filter(Event.id == reg.event_id).first()
        result.append(registration_to_out(reg, event, volunteer))
    return result


@router.post("/registrations/confirm", response_model=schemas.RegistrationOut)
def confirm_registration(body: schemas.RegistrationConfirm, db: Session = Depends(get_db)):
    reg = confirm_by_token(db, body.token)
    event = db.query(Event).filter(Event.id == reg.event_id).first()
    user = db.query(User).filter(User.id == reg.user_id).first()
    return registration_to_out(reg, event, user)
