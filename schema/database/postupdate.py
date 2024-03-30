
from pydantic import BaseModel
from typing import Optional

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    is_active: Optional[bool]

    class Config:
        orm_mode = True