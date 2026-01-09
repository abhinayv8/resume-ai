from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    text = Column(Text)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)

class Ranking(Base):
    __tablename__ = "rankings"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    score = Column(Float)


