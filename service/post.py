from database.event import Event
from sqlalchemy.orm import Session

from database.post import Post
from schema.database.postupdate import PostUpdate


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def delete(db: Session, post: Post):
    db.delete(post)
    db.commit()


def patch_post(db: Session, post_id: int, post_update: PostUpdate):
    db_post = get_post(db, post_id)
    if db_post:
        for field, value in post_update.dict(exclude_unset=True).items():
            setattr(db_post, field, value)
        db.commit()
        db.refresh(db_post)
        return db_post
    return None
