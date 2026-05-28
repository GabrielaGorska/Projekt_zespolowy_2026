"""Event helpers: slot counting and mapping ORM rows to API schemas."""

from sqlalchemy.orm import Session

from database.models import Event, EventRegistration, EventStatus, RegistrationStatus, User
from database.schemas import EventListOut, EventOut


def count_taken_slots(db: Session, event_id: int) -> int:
    """Slots occupied by pending or confirmed registrations."""
    return (
        db.query(EventRegistration)
        .filter(
            EventRegistration.event_id == event_id,
            EventRegistration.status.in_(
                [RegistrationStatus.PENDING, RegistrationStatus.CONFIRMED]
            ),
        )
        .count()
    )


def event_to_out(event: Event, db: Session, org_name: str | None = None) -> EventOut:
    taken = count_taken_slots(db, event.id)
    return EventOut(
        id=event.id,
        organization_id=event.organization_id,
        organization_name=org_name,
        title=event.title,
        description=event.description,
        location=event.location,
        category=event.category,
        start_date=event.start_date,
        end_date=event.end_date,
        max_slots=event.max_slots,
        status=event.status,
        created_at=event.created_at,
        taken_slots=taken,
        free_slots=max(0, event.max_slots - taken),
    )


def event_to_list_item(event: Event, db: Session, org_name: str | None = None) -> EventListOut:
    taken = count_taken_slots(db, event.id)
    return EventListOut(
        id=event.id,
        title=event.title,
        location=event.location,
        start_date=event.start_date,
        organization_name=org_name,
        status=event.status,
        max_slots=event.max_slots,
        taken_slots=taken,
        free_slots=max(0, event.max_slots - taken),
    )


def get_org_name(db: Session, org_id: int) -> str | None:
    org = db.query(User).filter(User.id == org_id).first()
    return org.organization_name if org else None


def ensure_event_open(event: Event):
    if event.status != EventStatus.ACTIVE:
        raise ValueError("Event is not open for registration")
