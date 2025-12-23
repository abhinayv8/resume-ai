from fastapi import APIRouter
from app.services.extractor_service import (
    extract_resume_entities,
    extract_job_entities
)
from app.services.matching_service import compute_match_score

router = APIRouter()

@router.post("/match")
async def match_resume_to_job(resume_text: str, job_text: str):
    resume_entities = extract_resume_entities(resume_text)
    job_entities = extract_job_entities(job_text)

    result = compute_match_score(resume_entities, job_entities)

    return {
        "match_score": result["score"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"]
    }
