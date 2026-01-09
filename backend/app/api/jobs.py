from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models

router = APIRouter()

@router.post("/")
def create_job(title: str, description: str, db: Session = Depends(get_db)):
    job = models.Job(title=title, description=description)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.get("/")
def list_jobs(db: Session = Depends(get_db)):
    return db.query(models.Job).all()
