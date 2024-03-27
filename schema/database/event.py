from sqlalchemy import Column, Integer, String

from infrastructure.mysql import Base

class Event(Base):
    __tablename__ = 'events'

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer)
    name: str = Column(String, unique=True)
    date: str = Column(String)
    content: str = Column(String)

