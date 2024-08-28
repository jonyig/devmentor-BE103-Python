from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from infrastructure.mysql import get_db
from schema.database.event import EventCreate
from services.auth import get_current_user

from services.event_service import EventService

router = APIRouter(
    tags=["events"],
    prefix="/events"
)


def get_event_service(db: Session = Depends(get_db)) -> EventService:
    return EventService(db=db)


@router.get("/")
def list_event(skip: int = 0, limit: int = 100, service: EventService = Depends(get_event_service)):
    return service.list_event(skip=skip, limit=limit)


@router.post("/")
def create_event(user: Annotated[dict, Depends(get_current_user)], event: EventCreate, service: EventService = Depends(get_event_service)):
    return service.create_event(user=user, event=event)
    

@router.delete("/{event_id}")
def delete_event_by_id(user: Annotated[dict, Depends(get_current_user)], event_id:int, service:EventService = Depends(get_event_service)):
    event = service.delete_event_by_id(user=user, event_id=event_id)
    if event == None: 
        raise HTTPException(status_code=404, detail="Event Not Found")
    return event


@router.put("/{event_id}")
def update_event_by_id(user: Annotated[dict, Depends(get_current_user)],event_id: int, event: EventCreate, service:EventService = Depends(get_event_service)):
    event = service.update_event_by_id(user=user, event_id=event_id, event=event)
    if event == None:
        raise HTTPException(status_code=404, detail="Event Not Found")
    return event