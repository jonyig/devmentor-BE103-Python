from sqlalchemy import Column, Integer, String

from infrastructure.mysql import Base

class User(Base):
    __tablename__ = 'users'

    id= Column(Integer, primary_key=True)
    lang_id = Column(Integer)
    username = Column(String, unique=True)



class UserWithPassword(User):
    password = Column(String)