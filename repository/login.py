from sqlalchemy.orm import Session
from schema.database.userfordb import User


def search(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

