from fastapi import FastAPI
from app.api import resumes

app = FastAPI(title="AI Resume Screening Platform")

app.include_router(
    resumes.router,
    prefix="/api/v1/resumes",
    tags=["Resumes"]
)
