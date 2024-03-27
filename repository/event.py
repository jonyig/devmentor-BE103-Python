from sqlalchemy.orm import Session
from database.event import Event


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()


# def create(db: Session, post: PostCreate):
#     db_user = Post(title=post.title, content=post.content)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()
#
#
# def delete(db: Session, post: Post):
#     db.delete(post)
#     db.commit()
#
#
# def patch_post(db: Session, post_id: int, post_update: PostUpdate):
#     db_post = get_post(db, post_id)
#     if db_post:
#         for field, value in post_update.dict(exclude_unset=True).items():
#             setattr(db_post, field, value)
#         db.commit()
#         db.refresh(db_post)
#         return db_post
#     return None