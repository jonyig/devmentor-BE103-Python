from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import service.post
from infrastructure.mysql import get_db
from schema.database.post import PostCreate

router = APIRouter(
    tags=["post"],
    prefix="/posts"
)


@router.get("/")
def list_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = service.post.lists(db, skip=skip, limit=limit)
    return posts


@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return service.post.create(db=db, post=post)
