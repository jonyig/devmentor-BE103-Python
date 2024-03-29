from sqlalchemy.orm import Session

from database.post import Post
from schema.database.post import PostCreate


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create(db: Session, post: PostCreate):
    db_user = Post(title=post.title, content=post.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user