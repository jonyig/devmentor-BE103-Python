from pydantic import BaseModel

class EventBase(BaseModel):
    user_id: int
    name: str
    date: str
    content: str | None = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
