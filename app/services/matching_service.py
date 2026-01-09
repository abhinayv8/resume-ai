from typing import Dict, List

def compute_match_score(
    resume_entities: Dict,
    job_entities: Dict
) -> Dict:
    resume_skills = set(resume_entities.get("skills", []))
    job_skills = set(job_entities.get("skills", []))

    if not job_skills:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "reason": "No skills found in job description"
        }

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    score = round((len(matched_skills) / len(job_skills)) * 100, 2)

    return {
        "score": score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
