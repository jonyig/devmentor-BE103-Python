from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import repository.event
from infrastructure.mysql import get_db
from schema.database.event import EventCreate, EventUpdate

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


@router.post("")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return repository.event.create(db=db, event=event)


@router.delete("/{event_id}")
def delete(event_id: int, db: Session = Depends(get_db)):
    event = repository.event.get_event(db, event_id)
    return repository.event.delete(db=db, event=event)


@router.patch("/{event_id}")
def update_event(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
    existing_event = repository.event.get_event(db, event_id)
    if existing_event is None:
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post = repository.event.patch_event(db, event_id, event_update)
    return updated_post

