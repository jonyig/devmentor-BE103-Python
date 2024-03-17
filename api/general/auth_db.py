from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from infrastructure.mysql import get_db
from service.auth import validate_login


router = APIRouter(
    tags=["auth_db"],
    prefix="/auth_db"
)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = validate_login(db, form_data.username, form_data.password)
    return {"access_token": user.username, "token_type": "bearer"}

