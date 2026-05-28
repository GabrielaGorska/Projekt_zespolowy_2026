"""Secure random tokens for password reset and registration email links."""

import secrets
from datetime import datetime, timedelta


def generate_token() -> str:
    return secrets.token_urlsafe(32)


def expiry_from_minutes(minutes: int) -> datetime:
    return datetime.utcnow() + timedelta(minutes=minutes)
