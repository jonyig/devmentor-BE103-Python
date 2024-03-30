from sqlalchemy.orm import Session
from database.user import User,UserWithPassword

def get_user(db: Session, username: str):
    return db.query(UserWithPassword).filter(UserWithPassword.username == username).first()

def get_user_data(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()