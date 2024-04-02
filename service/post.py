from sqlalchemy.orm import Session
from schema.database.postupdate import PostUpdate
from schema.database.post import Post
from repository.post import patch_post, get_post
from repository.post import delete as delete_post_repo

def patch(db: Session, post_id: int, post_update: PostUpdate):
    existing_post = get_post(db, post_id)
    if existing_post is None:
        return None
    return patch_post(db, post_id, post_update)

def get_post_by_id(db: Session, post_id: int):
    return get_post(db, post_id)

def delete(db: Session, post: Post):
    delete_post_repo(db=db, post=post)