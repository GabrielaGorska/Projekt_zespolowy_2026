"""Password reset and JWT login response schemas."""

from pydantic import BaseModel, EmailStr, Field


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
