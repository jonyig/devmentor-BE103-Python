from pydantic import BaseModel

class SubscribeBase(BaseModel):
    user_id: int

    class Config:
        orm_mode = True
