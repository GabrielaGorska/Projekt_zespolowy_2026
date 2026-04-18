import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum
from .connections import Base


class UserRole(enum.Enum):
    """Roles for different types of users in the system."""
    VOLUNTEER = "volunteer"
    ORGANIZATION = "organization"
    ADMIN = "admin"


class User(Base):
    """The main User table for the MySQL database."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.VOLUNTEER)

    # Status fields
    is_active = Column(Boolean, default=True)
    is_approved = Column(Boolean, default=False)  # For organizations
