import re

def extract_resume_entities(text: str):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phones = re.findall(r"\+?\d[\d\s\-]{8,}\d", text)

    skills_list = [
        "python", "java", "javascript", "fastapi",
        "django", "flask", "react", "node",
        "sql", "postgresql", "mongodb",
        "aws", "docker", "kubernetes",
        "git", "linux",
    ]

    text_lower = text.lower()
    skills = [s for s in skills_list if s in text_lower]

    return {
        "email": emails[0] if emails else None,
        "phone": phones[0] if phones else None,
        "skills": skills,
    }

def extract_job_entities(text: str):
    skills_list = [
        "python", "java", "javascript", "fastapi",
        "django", "flask", "react", "node",
        "sql", "postgresql", "mongodb",
        "aws", "docker", "kubernetes",
        "git", "linux",
    ]

    text_lower = text.lower()
    skills = [s for s in skills_list if s in text_lower]

    return {"skills": skills}
