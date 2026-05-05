"""Shared page/page_size query params and SQLAlchemy offset/limit helper."""

from typing import TypeVar

from fastapi import Query
from sqlalchemy.orm import Query as SAQuery

T = TypeVar("T")

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100


def pagination_params(
    page: int = Query(1, ge=1, description="Page number (1-based)"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
):
    return {"page": page, "page_size": page_size, "skip": (page - 1) * page_size}


def paginate_query(query: SAQuery, skip: int, limit: int):
    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return items, total
