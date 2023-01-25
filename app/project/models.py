import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Project(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    start: str = Field(...)
    end: str = Field(...)
    desc: str = Field(...)

class ProjectUpdate(BaseModel):
    name: Optional[str]
    start: Optional[str]
    end: Optional[str]
    desc: Optional[str]
