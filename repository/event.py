from sqlalchemy.orm import Session

from database.event import Event
from database.subscribe import Subscribe
from schema.database.event import EventCreate, EventUpdate
from schema.database.subscribe import SubscribeBase


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()


def create(db: Session, event: EventCreate):
    db_user = Event(user_id=event.user_id, name=event.name, date=event.date, content=event.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


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

def subscribe(db: Session, event_id: int, subscribe: SubscribeBase):
    db_subscribe = Subscribe(user_id=subscribe.user_id, event_id=event_id)
    db.add(db_subscribe)
    db.commit()
    db.refresh(db_subscribe)
    return db_subscribe

def get_subscriptions(db: Session, user_id: int):
    return db.query(Subscribe).filter(Subscribe.user_id == user_id).all()
