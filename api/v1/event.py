from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import repository.event
from infrastructure.mysql import get_db

router = APIRouter(
    tags=["event"],
    prefix="/events"
)


# 獲取全部 （get) /v1/events
# 獲取單個 （get)  /v1/events/(/{event_id})
@router.get("")
def list_event(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = repository.event.lists(db, skip=skip, limit=limit)
    return events



@router.get("/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = repository.event.get_event(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return event



# @router.post("", tags=["Post"])
# def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     return repository.post.create(db=db, post=post)
#
#
# @router.delete("/{post_id}", tags=["Post"])
# def delete(post_id: int, db: Session = Depends(get_db)):
#     post = repository.post.get_post(db, post_id)
#     return repository.post.delete(db=db, post=post)
#
#
# @router.patch("/{post_id}", tags=["Post"])
# def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
#     existing_post = repository.post.get_post(db, post_id)
#     if existing_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     updated_post = repository.post.patch_post(db, post_id, post_update)
#     return updated_post
#
