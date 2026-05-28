"""CSV export for organizers (participants) and administrators (bulk data)."""

import csv
import io
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from database.connections import get_db
from database.models import Event, EventRegistration, RegistrationStatus, User, UserRole
from utils.dependencies import ensure_event_owner, get_current_admin, get_current_organization

router = APIRouter(prefix="/export", tags=["Export"])


def _csv_response(rows: list[list], filename: str) -> StreamingResponse:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    for row in rows:
        writer.writerow(row)
    buffer.seek(0)
    return StreamingResponse(
        iter([buffer.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/events/{event_id}/participants.csv")
def export_participants(
    event_id: int,
    org: User = Depends(get_current_organization),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    ensure_event_owner(event.organization_id, org)

    rows = [["first_name", "last_name", "email", "registered_at", "status"]]
    regs = (
        db.query(EventRegistration)
        .filter(
            EventRegistration.event_id == event_id,
            EventRegistration.status != RegistrationStatus.CANCELLED,
        )
        .all()
    )
    for reg in regs:
        u = db.query(User).filter(User.id == reg.user_id).first()
        rows.append([
            u.first_name or "",
            u.last_name or "",
            u.email if u else "",
            reg.registered_at.isoformat(),
            reg.status.value,
        ])
    return _csv_response(rows, f"participants_event_{event_id}.csv")


@router.get("/admin/users.csv")
def export_users_admin(
    _: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
    role: Optional[UserRole] = Query(None),
):
    q = db.query(User)
    if role:
        q = q.filter(User.role == role)
    rows = [["email", "role", "is_active", "is_approved", "organization_name", "nip"]]
    for u in q.all():
        rows.append([
            u.email,
            u.role.value,
            str(u.is_active),
            str(u.is_approved),
            u.organization_name or "",
            u.nip or "",
        ])
    return _csv_response(rows, "users.csv")


@router.get("/admin/events.csv")
def export_events_admin(_: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    rows = [["id", "title", "organization_id", "start_date", "location", "max_slots", "status"]]
    for e in db.query(Event).all():
        rows.append([
            e.id,
            e.title,
            e.organization_id,
            e.start_date.isoformat(),
            e.location,
            e.max_slots,
            e.status.value,
        ])
    return _csv_response(rows, "events.csv")


@router.get("/admin/registrations.csv")
def export_registrations_admin(
    _: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    rows = [["event_id", "user_email", "status", "registered_at"]]
    for reg in db.query(EventRegistration).all():
        u = db.query(User).filter(User.id == reg.user_id).first()
        rows.append([
            reg.event_id,
            u.email if u else "",
            reg.status.value,
            reg.registered_at.isoformat(),
        ])
    return _csv_response(rows, "registrations.csv")
