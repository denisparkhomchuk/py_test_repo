from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    content: str
    user_id: str
    is_done: bool
    task_id: Optional[str] = None
