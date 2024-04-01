from database.event import Event
from sqlalchemy.orm import Session
from schema.database.event import EventUpdate


def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()


def delete(db: Session, event: Event):
    db.delete(event)
    db.commit()


def patch_event(db: Session, event_id: int, event_update: EventUpdate):
    db_event = get_event(db, event_id)
    if db_event:
        for field, value in event_update.dict(exclude_unset=True).items():
            setattr(db_event, field, value)
        db.commit()
        db.refresh(db_event)
        return db_event
    return None
