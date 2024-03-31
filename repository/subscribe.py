from sqlalchemy.orm import Session
from database.userevent import UserEvent
from schema.database.subscribe import SubscribeBase


def subscribe(db: Session, event_id: int, subscribe: SubscribeBase):
    db_subscribe = UserEvent(user_id=subscribe.user_id, event_id=event_id)
    db.add(db_subscribe)
    db.commit()
    db.refresh(db_subscribe)
    return db_subscribe

def get_subscriptions(db: Session, user_id: int):
    return db.query(UserEvent).filter(UserEvent.user_id == user_id).all()
