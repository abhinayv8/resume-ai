from fastapi import APIRouter
from app.services.extractor_service import (
    extract_resume_entities,
    extract_job_entities
)
from app.services.matching_service import compute_match_score
from app.services.embedding_service import compute_semantic_similarity
from app.services.hybrid_scoring import hybrid_score

router = APIRouter()

@router.post("/match")
async def match_resume_to_job(resume_text: str, job_text: str):
    resume_entities = extract_resume_entities(resume_text)
    job_entities = extract_job_entities(job_text)

    skill_result = compute_match_score(resume_entities, job_entities)
    semantic_score = compute_semantic_similarity(resume_text, job_text)

    final_score = hybrid_score(
        skill_result["score"],
        semantic_score
    )

    return {
        "skill_score": skill_result["score"],
        "semantic_score": semantic_score,
        "final_score": final_score,
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"]
    }
