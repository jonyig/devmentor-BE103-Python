from sqlalchemy import Column, Integer, String

from infrastructure.mysql import Base

class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    lang_id: int = Column(Integer)
    username: str = Column(String, unique=True)



class UserWithPassword(User):
    password: str = Column(String)