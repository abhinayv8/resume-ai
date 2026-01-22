from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.analytics_service import platform_overview, job_overview

router = APIRouter()

@router.get("/overview")
def get_platform_overview(db: Session = Depends(get_db)):
    return platform_overview(db)

@router.get("/job/{job_id}")
def get_job_overview(job_id: int, db: Session = Depends(get_db)):
    return job_overview(db, job_id)


