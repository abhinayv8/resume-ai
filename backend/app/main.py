from fastapi import FastAPI
from app.api import resumes, match

app = FastAPI(title="AI Resume Screening Platform")

app.include_router(
    resumes.router,
    prefix="/api/v1/resumes",
    tags=["Resumes"]
)

app.include_router(
    match.router,
    prefix="/api/v1/match",
    tags=["Matching"]
)

