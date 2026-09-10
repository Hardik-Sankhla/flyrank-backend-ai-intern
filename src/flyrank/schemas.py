from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the task")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, description="The title of the task")
    done: Optional[bool] = Field(None, description="The status of the task")
