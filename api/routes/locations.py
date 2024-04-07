from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Locations
from database.lifespan import engine

locations_router = APIRouter()


def get_session():
    """
    Function to get a database session using the engine defined in the lifespan module.

    Returns:
        Session: A SQLModel session object.
    """
    with Session(engine) as session:
        yield session


@locations_router.get("/")
def get_all(session: Session = Depends(get_session)):
    """
    Endpoint to get all locations.

    Returns:
        List[Locations]: A list of all locations.
    """
    locations = session.exec(select(Locations)).all()
    return locations


@locations_router.get("/{location_id}")
def get_by_id(location_id: int, session: Session = Depends(get_session)):
    """
    Endpoint to get a location by its ID.

    Args:
        location_id (int): The ID of the location.

    Returns:
        Locations: The location with the specified ID.

    Raises:
        HTTPException: If the location with the specified ID is not found.
    """
    location = session.get(Locations, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location
