from sqlalchemy.orm import Session
from schema.database.event import EventUpdate, Event
from repository.event import patch_event, get_event
from repository.event import delete as delete_event_repo

def patch(db: Session, event_id: int, event_update: EventUpdate):
    existing_event = get_event(db, event_id)
    if existing_event is None:
        return None
    return patch_event(db, event_id, event_update)

def get_event_by_id(db: Session, event_id: int):
    return get_event(db, event_id)

def delete(db: Session, event: Event):
    delete_event_repo(db=db, event=event)