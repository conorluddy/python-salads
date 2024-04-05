from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Locations
from database.lifespan import engine

locations_router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@locations_router.get("/")
def get_all(session: Session = Depends(get_session)):
    locations = session.exec(select(Locations)).all()
    return locations


@locations_router.get("/{location_id}")
def get_by_id(location_id: int, session: Session = Depends(get_session)):
    location = session.get(Locations, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location
