from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.connections import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="LSWIS API",
    description="System wspomagania i zarządzania wolontariatem",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins, adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/db-test", tags=["Debug"])
def test_db_connection(db: Session = Depends(get_db)):
    """
    Test endpoint to verify database connectivity.
    """
    try:
        # Execute a simple SQL query to check connection
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "success"}
    except Exception as e:
        # If connection fails, return 500 error with details
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )
