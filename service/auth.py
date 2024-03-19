from fastapi import HTTPException
from schema.database.users import User
from sqlalchemy.orm import Session
from repository.users import search

def validate_login(db: Session, form_data_username: str, form_data_password: str) -> tuple[User, str]:
    user = search(db, form_data_username)
    if not user:
        return User(), "Incorrect username or password"
    if not form_data_password == user.password:
        return User(), "Incorrect username or password"
    return user, ""