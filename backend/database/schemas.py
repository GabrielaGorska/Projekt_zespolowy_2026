from pydantic import BaseModel, EmailStr, Field
from .models import UserRole


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


class UserOut(UserBase):
    id: int
    role: UserRole
    is_active: bool
    is_approved: bool

    class ConfigDict:
        from_attributes = True
