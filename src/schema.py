from pydantic import BaseModel
from typing import Optional
from enum import Enum

class WorkArrangement(str, Enum):
    remote = "remote"
    hybrid = "hybrid"
    onsite = "onsite"

class JobPosting(BaseModel):
    title: str
    company: str
    location: str
    work_arrangement: WorkArrangement 
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    employment_type: Optional[int] = None
    years_experience_min: Optional[int] = None
    seniority_level: Optional[str] = None
    requirements: list[str]
    skills: list[str]
    benefits: Optional[list[str]] = None
    