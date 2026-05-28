"""User registration, login, profile, and public user DTOs."""

from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from database.models import UserRole


class UserBase(BaseModel):
    email: EmailStr


class VolunteerCreate(UserBase):
    first_name: str
    last_name: str
    password: str = Field(..., min_length=8)


class OrganizationCreate(UserBase):
    organization_name: str
    nip: str = Field(..., min_length=10, max_length=10)
    address: str
    contact_person: str
    phone: str
    password: str = Field(..., min_length=8)


class UserLogin(UserBase):
    password: str


class UserProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    organization_name: Optional[str] = None
    address: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None


class UserOut(UserBase):
    id: int
    role: UserRole
    is_active: bool
    is_approved: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    organization_name: Optional[str] = None
    nip: Optional[str] = None
    address: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None

    model_config = {"from_attributes": True}
