from sqlalchemy import Boolean, Column, Integer, String
from infrastructure.mysql import Base


class UserEvent(Base):
    __tablename__ = 'users_events'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    event_id = Column(Integer)


