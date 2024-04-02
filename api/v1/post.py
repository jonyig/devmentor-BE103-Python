from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import service.post
import repository.post
from schema.database.postupdate import PostUpdate
from infrastructure.mysql import get_db
from schema.database.post import PostCreate

router = APIRouter(
    tags=["post"],
    prefix="/posts"
)


@router.get("")
def list_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = repository.post.lists(db, skip=skip, limit=limit)
    return posts


@router.post("")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return repository.post.create(db=db, post=post)


@router.delete("/{post_id}")
def delete(post_id: int, db: Session = Depends(get_db)):
    post = service.post.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return service.post.delete(db=db, post=post)


@router.patch("/{post_id}")
def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
    existing_post = service.post.get_post_by_id(db, post_id)
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post = service.post.patch(db, post_id, post_update)
    return updated_post


@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = service.post.get_post_by_id(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
