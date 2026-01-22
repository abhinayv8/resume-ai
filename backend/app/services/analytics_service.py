from sqlalchemy.orm import Session
from app.db import models

def platform_overview(db: Session):
    total_resumes = db.query(models.Resume).count()
    total_jobs = db.query(models.Job).count()
    total_rankings = db.query(models.Ranking).count()

    scores = [s[0] for s in db.query(models.Ranking.score).all()]
    avg_score = round(sum(scores) / len(scores), 2) if scores else 0

    return {
        "total_resumes": total_resumes,
        "total_jobs": total_jobs,
        "total_rankings": total_rankings,
        "average_match_score": avg_score,
    }

def job_overview(db: Session, job_id: int):
    rankings = (
        db.query(models.Ranking)
        .filter(models.Ranking.job_id == job_id)
        .all()
    )

    if not rankings:
        return {
            "job_id": job_id,
            "candidates": 0,
            "average_score": 0,
            "top_candidates": [],
        }

    scores = [r.score for r in rankings]
    avg_score = round(sum(scores) / len(scores), 2)

    top = sorted(rankings, key=lambda r: r.score, reverse=True)[:5]

    return {
        "job_id": job_id,
        "candidates": len(rankings),
        "average_score": avg_score,
        "top_candidates": [
            {"resume_id": r.resume_id, "score": r.score} for r in top
        ],
    }

def skill_gap_analysis(db: Session, job_id: int):
    rankings = (
        db.query(models.Ranking)
        .filter(models.Ranking.job_id == job_id)
        .all()
    )

    if not rankings:
        return {
            "job_id": job_id,
            "missing_skills": [],
        }

    resumes = (
        db.query(models.Resume.text)
        .join(models.Ranking, models.Ranking.resume_id == models.Resume.id)
        .filter(models.Ranking.job_id == job_id)
        .all()
    )

    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if not job:
        return {"job_id": job_id, "missing_skills": []}

    job_text = job.description.lower()

    skill_keywords = [
        "python", "java", "javascript", "fastapi", "django",
        "flask", "react", "node", "sql", "postgresql",
        "mongodb", "aws", "docker", "kubernetes", "git", "linux",
    ]

    missing_counts = {}

    for skill in skill_keywords:
        if skill not in job_text:
            continue

        missing = 0
        for (resume_text,) in resumes:
            if skill not in resume_text.lower():
                missing += 1

        if missing > 0:
            missing_counts[skill] = missing

    return {
        "job_id": job_id,
        "missing_skills": sorted(
            missing_counts.items(),
            key=lambda x: x[1],
            reverse=True,
        ),
    }
