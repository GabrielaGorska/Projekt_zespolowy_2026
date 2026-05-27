"""Admin panel API - users, organizations, events, registrations oversight."""

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import schemas
from database.connections import get_db
from database.models import Event, EventRegistration, User, UserRole
from utils.dependencies import get_current_admin
from utils.pagination import paginate_query, pagination_params

router = APIRouter(prefix="/admin", tags=["Admin Management"])


@router.get("/users", response_model=schemas.PaginatedResponse[schemas.UserOut])
def list_users(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
    page_params: dict = Depends(pagination_params),
    role: Optional[UserRole] = Query(None),
    pending_only: bool = Query(False, description="Only unapproved organizations"),
):
    q = db.query(User)
    if role:
        q = q.filter(User.role == role)
    if pending_only:
        q = q.filter(User.role == UserRole.ORGANIZATION, User.is_approved.is_(False))
    q = q.order_by(User.id)
    users, total = paginate_query(q, page_params["skip"], page_params["page_size"])
    return schemas.PaginatedResponse(
        items=users,
        total=total,
        page=page_params["page"],
        page_size=page_params["page_size"],
    )


@router.patch("/approve-organization/{user_id}", response_model=schemas.UserOut)
def approve_organization(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != UserRole.ORGANIZATION:
        raise HTTPException(status_code=400, detail="User is not an organization")
    if user.is_approved:
        raise HTTPException(status_code=400, detail="Organization already approved")
    user.is_approved = True
    db.commit()
    db.refresh(user)
    return user


@router.patch("/reject-organization/{user_id}", response_model=schemas.UserOut)
def reject_organization(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != UserRole.ORGANIZATION:
        raise HTTPException(status_code=400, detail="User is not an organization")
    user.is_approved = False
    user.is_active = False
    db.commit()
    db.refresh(user)
    return user


@router.patch("/users/{user_id}/block", response_model=schemas.UserOut)
def block_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot block your own account")
    user.is_active = False
    db.commit()
    db.refresh(user)
    return user


@router.patch("/users/{user_id}/unblock", response_model=schemas.UserOut)
def unblock_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = True
    db.commit()
    db.refresh(user)
    return user


@router.patch("/promote/{user_id}", response_model=schemas.UserOut)
def promote_to_admin(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role = UserRole.ADMIN
    user.is_approved = True
    db.commit()
    db.refresh(user)
    return user


@router.get("/events", response_model=List[schemas.EventOut])
def admin_list_events(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    from services.events import event_to_out, get_org_name

    events = db.query(Event).order_by(Event.start_date.desc()).all()
    return [event_to_out(e, db, get_org_name(db, e.organization_id)) for e in events]


@router.get("/registrations", response_model=List[schemas.RegistrationOut])
def admin_list_registrations(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    from services.registrations import registration_to_out

    regs = db.query(EventRegistration).order_by(EventRegistration.registered_at.desc()).all()
    out = []
    for reg in regs:
        event = db.query(Event).filter(Event.id == reg.event_id).first()
        user = db.query(User).filter(User.id == reg.user_id).first()
        out.append(registration_to_out(reg, event, user))
    return out
