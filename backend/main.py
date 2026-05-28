"""FastAPI application entry point — wires routers and creates DB tables on startup."""

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from database.connections import Base, engine, get_db
from database import models  # noqa: F401 - import registers all ORM models with Base
from routers import admin, auth, events, export, profile, registrations

# Dev bootstrap: creates tables if missing (use Alembic in production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LSWIS API",
    description="System wspomagania i zarządzania wolontariatem",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTP routes grouped by domain (see routers/*.py)
app.include_router(auth.router)           # register, login, password reset
app.include_router(profile.router)        # update own profile
app.include_router(events.router)         # CRUD events, public list
app.include_router(registrations.router)  # sign-up, cancel, confirm email
app.include_router(admin.router)          # users, approve/block orgs
app.include_router(export.router)         # CSV downloads


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


@app.get("/db-test", tags=["Debug"])
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connection OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
