import uuid
from datetime import date
from typing import Optional, Dict
from pydantic import BaseModel, Field, Json

class AnyJson(BaseModel):
    data: Dict

class Project(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    start: date  = Field(...)
    end: date = Field(...)
    desc: str = Field(...)

class ProjectUpdate(BaseModel):
    name: Optional[str]
    start: Optional[date]
    end: Optional[date]
    desc: Optional[str]
