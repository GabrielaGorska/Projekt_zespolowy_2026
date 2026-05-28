import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String

from database.connections import Base


class UserRole(enum.Enum):
    VOLUNTEER = "volunteer"
    ORGANIZATION = "organization"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.VOLUNTEER, nullable=False)

    is_active = Column(Boolean, default=True)
    is_approved = Column(Boolean, default=False)

    # Volunteer profile (nullable for other roles)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)

    # Organization profile (nullable for other roles)
    organization_name = Column(String(255), nullable=True)
    nip = Column(String(10), unique=True, index=True, nullable=True)
    address = Column(String(500), nullable=True)
    contact_person = Column(String(200), nullable=True)
    phone = Column(String(20), nullable=True)
