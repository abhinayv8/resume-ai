import re
from typing import Dict, List, Optional

def extract_resume_entities(text: str) -> Dict[str, Optional[str | List[str]]]:
    """
    Extracts basic structured information from resume text.
    Deterministic, rule-based (no ML yet).
    """

    # Email extraction
    emails = re.findall(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        text
    )

    # Phone number extraction
    phones = re.findall(
        r"\+?\d[\d\s\-]{8,}\d",
        text
    )

    # Skill keyword matching (extend later)
    skill_keywords = [
        "python", "java", "javascript", "fastapi",
        "django", "flask", "react", "node",
        "sql", "postgresql", "mongodb",
        "aws", "docker", "kubernetes",
        "git", "linux"
    ]

    text_lower = text.lower()
    skills = [skill for skill in skill_keywords if skill in text_lower]

    return {
        "email": emails[0] if emails else None,
        "phone": phones[0] if phones else None,
        "skills": skills
    }

def extract_job_entities(text: str) -> Dict:
    """
    Extracts structured information from a job description.
    """
    skill_keywords = [
        "python", "java", "javascript", "fastapi",
        "django", "flask", "react", "node",
        "sql", "postgresql", "mongodb",
        "aws", "docker", "kubernetes",
        "git", "linux"
    ]

    text_lower = text.lower()
    skills = [skill for skill in skill_keywords if skill in text_lower]

    return {
        "skills": skills
    }

