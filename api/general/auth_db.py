from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

# 創建一個 CryptContext 對象，用於管理密碼哈希化
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 資料庫連線
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:1234@127.0.0.1:3308/be103"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 定義基礎模型
Base = declarative_base()

# 定義用戶模型
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# 創建資料庫表格
Base.metadata.create_all(bind=engine)

# FastAPI 實例
app = FastAPI()

# OAuth2 密碼認證
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 模擬驗證密碼的函式
def verify_password(plain_password, hashed_password):
    # 使用 verify() 方法來比較明文密碼和哈希密碼是否匹配
    return pwd_context.verify(plain_password, hashed_password)

# 依賴注入，用於取得資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 登入路由
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    query = db.query(User).filter(User.username == form_data.username)
    user = query.first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 返回 token
    return {"access_token": user.username, "token_type": "bearer"}
