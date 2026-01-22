from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.services.ranking_service import rank_resumes
from app.db.session import get_db
from app.db import models
from fastapi import Body


router = APIRouter()

class RankingRequest(BaseModel):
    resumes: List[str]
    job_text: str

@router.post("/rank/{job_id}")
def rank_candidates(
    job_id: int,
    payload: RankingRequest = Body(...),
    db: Session = Depends(get_db)
):

    ranked = rank_resumes(payload.resumes, payload.job_text)

    for r in ranked:
        db.add(
            models.Ranking(
                job_id=job_id,
                resume_id=r["resume_id"],
                score=r["score"],
            )
        )

    db.commit()

    return {
    "ranked_candidates": ranked
}


@router.get("/job/{job_id}")
def get_job_rankings(job_id: int, db: Session = Depends(get_db)):
    return (
        db.query(models.Ranking)
        .filter(models.Ranking.job_id == job_id)
        .order_by(models.Ranking.score.desc())
        .all()
    )

