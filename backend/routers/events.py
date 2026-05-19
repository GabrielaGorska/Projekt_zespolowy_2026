"""Events CRUD, public listing with filters, organization-owned events."""

from datetime import datetime
from typing import Optional

from utils.datetime_utils import is_in_past, to_utc_naive

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import schemas
from database.connections import get_db
from database.models import Event, EventStatus, User, UserRole
from services.events import event_to_list_item, event_to_out, get_org_name
from utils.dependencies import (
    ensure_event_owner,
    get_current_active_user,
    get_current_organization,
)
from utils.pagination import paginate_query, pagination_params

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("", response_model=schemas.EventOut, status_code=201)
def create_event(
    data: schemas.EventCreate,
    org: User = Depends(get_current_organization),
    db: Session = Depends(get_db),
):
    if is_in_past(data.start_date):
        raise HTTPException(status_code=400, detail="start_date cannot be in the past")

    event = Event(
        organization_id=org.id,
        title=data.title,
        description=data.description,
        location=data.location,
        category=data.category,
        start_date=to_utc_naive(data.start_date),
        end_date=to_utc_naive(data.end_date) if data.end_date else None,
        max_slots=data.max_slots,
        status=EventStatus.ACTIVE,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event_to_out(event, db, org.organization_name)


@router.get("", response_model=schemas.PaginatedResponse[schemas.EventListOut])
def list_events(
    db: Session = Depends(get_db),
    page_params: dict = Depends(pagination_params),
    date_from: Optional[datetime] = Query(None),
    date_to: Optional[datetime] = Query(None),
    category: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    organization_id: Optional[int] = Query(None),
    status: Optional[EventStatus] = Query(EventStatus.ACTIVE),
):
    q = db.query(Event)
    if status:
        q = q.filter(Event.status == status)
    if date_from:
        q = q.filter(Event.start_date >= date_from)
    if date_to:
        q = q.filter(Event.start_date <= date_to)
    if category:
        q = q.filter(Event.category.ilike(f"%{category}%"))
    if location:
        q = q.filter(Event.location.ilike(f"%{location}%"))
    if organization_id:
        q = q.filter(Event.organization_id == organization_id)

    q = q.order_by(Event.start_date.asc())
    events, total = paginate_query(q, page_params["skip"], page_params["page_size"])
    items = [
        event_to_list_item(e, db, get_org_name(db, e.organization_id)) for e in events
    ]
    return schemas.PaginatedResponse(
        items=items,
        total=total,
        page=page_params["page"],
        page_size=page_params["page_size"],
    )


@router.get("/mine", response_model=list[schemas.EventOut])
def my_organization_events(
    org: User = Depends(get_current_organization),
    db: Session = Depends(get_db),
):
    events = db.query(Event).filter(Event.organization_id == org.id).order_by(Event.start_date).all()
    return [event_to_out(e, db, org.organization_name) for e in events]


@router.get("/{event_id}", response_model=schemas.EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event_to_out(event, db, get_org_name(db, event.organization_id))


@router.patch("/{event_id}", response_model=schemas.EventOut)
def update_event(
    event_id: int,
    data: schemas.EventUpdate,
    user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    ensure_event_owner(event.organization_id, user)

    updates = data.model_dump(exclude_unset=True)
    if "start_date" in updates and is_in_past(updates["start_date"]):
        raise HTTPException(status_code=400, detail="start_date cannot be in the past")
    for field, value in updates.items():
        if field in ("start_date", "end_date") and value is not None:
            value = to_utc_naive(value)
        setattr(event, field, value)
    db.commit()
    db.refresh(event)
    return event_to_out(event, db, get_org_name(db, event.organization_id))


@router.post("/{event_id}/close", response_model=schemas.EventOut)
def close_event(
    event_id: int,
    user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    ensure_event_owner(event.organization_id, user)
    event.status = EventStatus.CLOSED
    db.commit()
    db.refresh(event)
    return event_to_out(event, db, get_org_name(db, event.organization_id))
