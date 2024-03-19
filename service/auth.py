from schema.database.user import User
from sqlalchemy.orm import Session
from repository.users import get_user

def validate_login(db: Session, form_data_username: str, form_data_password: str) -> User:
    user = get_user(db, form_data_username)
    if not user:
        return None
    if not form_data_password == user.password:
        return False
    return user

def fake_decode_token(token, db: Session):
    user = db.query(User).filter(User.username == token).first()
    return user
