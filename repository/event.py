from sqlalchemy.orm import Session
from database.event import Event
from schema.database.event import EventCreate, EventUpdate



def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()


def create(db: Session, event: EventCreate):
    db_user = Event(user_id=event.user_id, name=event.name, date=event.date, content=event.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



