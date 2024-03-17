from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from infrastructure.mysql import get_db
from schema.database.userfordb import User


router = APIRouter(
    tags=["auth_db"],
    prefix="/auth_db"
)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    query = db.query(User).filter(User.username == form_data.username)
    user = query.first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not form_data.password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

