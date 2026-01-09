from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import resumes, jobs, ranking, analytics, match

app = FastAPI(title="AI Resume Screening Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resumes.router, prefix="/api/v1/resumes", tags=["Resumes"])
app.include_router(jobs.router, prefix="/api/v1/jobs", tags=["Jobs"])
app.include_router(ranking.router, prefix="/api/v1/ranking", tags=["Ranking"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
app.include_router(match.router, prefix="/api/v1/match", tags=["Matching"])


@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"healthy": True}




