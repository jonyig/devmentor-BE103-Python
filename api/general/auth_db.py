from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from infrastructure.mysql import get_db
from repository.login import search


router = APIRouter(
    tags=["auth_db"],
    prefix="/auth_db"
)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): #接受用戶給的http request&給回應(API Controller)
    user = search(db, form_data.username)
    if not user: #處理請求、計算、驗證等(?)在這裡是做比較formdata是否存在於db裡  (service)
        raise HTTPException(status_code=400, detail="Incorrect username or password")  #給回應(API controller)
    if not form_data.password == user.password: #service
        raise HTTPException(status_code=400, detail="Incorrect username or password") #給回應(API controller)

    return {"access_token": user.username, "token_type": "bearer"}

