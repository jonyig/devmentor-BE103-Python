from fastapi import HTTPException
from schema.database.userfordb import User
from sqlalchemy.orm import Session
from repository.login import search

def validate_login(db: Session, form_data_username: str, form_data_password: str) -> User:
    user = search(db, form_data_username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not form_data_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user