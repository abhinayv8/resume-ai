from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models

router = APIRouter()

from app.db.session import get_db

@router.get("/overview")
def analytics_overview(db: Session = Depends(get_db)):
    total_resumes = db.query(models.Resume).count()
    total_jobs = db.query(models.Job).count()
    scores = [s[0] for s in db.query(models.Ranking.score).all()]
    avg_score = sum(scores) / len(scores) if scores else 0
    return {
        "total_resumes": total_resumes,
        "total_jobs": total_jobs,
        "average_match_score": round(avg_score, 2),
    }



