from sqlalchemy.orm import Session

from database.post import Post
from database.postupdate import PostUpdate
from schema.database.post import PostCreate


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create(db: Session, post: PostCreate):
    db_user = Post(title=post.title, content=post.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def delete(db: Session, post: Post):
    db.delete(post)
    db.commit()


def patch_post(db: Session, post_id: int, post_update: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        for field, value in post_update.dict(exclude_unset=True).items():
            setattr(db_post, field, value)
        db.commit()
        db.refresh(db_post)
        return db_post
    return None