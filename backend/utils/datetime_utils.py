"""UTC datetime helpers - safe compare and store regardless of client timezone."""

from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def to_utc_aware(dt: datetime) -> datetime:
    """Normalize naive (assumed UTC) or aware datetimes to UTC aware."""
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def to_utc_naive(dt: datetime) -> datetime:
    """Store as naive UTC in MySQL DateTime columns."""
    return to_utc_aware(dt).replace(tzinfo=None)


def is_in_past(dt: datetime) -> bool:
    return to_utc_aware(dt) < utc_now()
