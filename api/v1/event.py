from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import service.event
import repository.event
import repository.subscribe
from infrastructure.mysql import get_db
from schema.database.event import EventCreate, EventUpdate
from schema.database.subscribe import SubscribeBase

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
    event = service.event.get_event_by_id(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return repository.event.create(db=db, event=event)


@router.delete("/{event_id}")
def delete(event_id: int, db: Session = Depends(get_db)):
    event = service.event.get_event(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return service.event.delete(db=db, event=event)


@router.patch("/{event_id}")
def update_event(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
    existing_event = service.event.get_event_by_id(db, event_id)
    if existing_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    updated_event = service.event.patch(db, event_id, event_update)
    return updated_event


@router.post("/{event_id}/subscribers")
def subscribe(event_id: int, subscribe: SubscribeBase, db: Session = Depends(get_db)):
    return repository.subscribe.subscribe(db=db, event_id=event_id, subscribe=subscribe)

@router.get("/users/{user_id}/subscriptions")
def get_subscriptions(user_id: int, db: Session = Depends(get_db)):
    user_subscriptions = repository.subscribe.get_subscriptions(db=db, user_id=user_id)
    return user_subscriptions
