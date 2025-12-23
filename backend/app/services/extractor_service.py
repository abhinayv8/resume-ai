import re
from typing import List, Dict

# Example skill vocabulary (expand later)
SKILL_KEYWORDS = [
    "python", "java", "c++", "javascript",
    "fastapi", "django", "flask",
    "sql", "postgresql", "mysql",
    "docker", "kubernetes",
    "aws", "azure", "gcp",
    "machine learning", "nlp", "data analysis"
]

EDUCATION_KEYWORDS = [
    "bachelor", "master", "phd",
    "b.tech", "m.tech", "b.sc", "m.sc",
    "computer science", "information technology"
]

def extract_skills(text: str) -> List[str]:
    text_lower = text.lower()
    return sorted(
        {skill for skill in SKILL_KEYWORDS if skill in text_lower}
    )

def extract_education(text: str) -> List[str]:
    text_lower = text.lower()
    return sorted(
        {edu for edu in EDUCATION_KEYWORDS if edu in text_lower}
    )

def extract_experience_years(text: str) -> float:
    """
    Extract experience like:
    - '3 years experience'
    - '2.5 yrs'
    - '5+ years'
    """
    matches = re.findall(
        r"(\d+(?:\.\d+)?)\s*(?:\+?\s*)?(?:years?|yrs?)",
        text.lower()
    )
    if not matches:
        return 0.0
    return max(float(m) for m in matches)

def extract_resume_entities(text: str) -> Dict:
    return {
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience_years": extract_experience_years(text)
    }
