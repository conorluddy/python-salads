from fastapi import FastAPI
from sqlmodel import Session
from database.lifespan import lifespan
from models.locations import LocationCreate, LocationRead
from database.lifespan import engine
from database.tables import Locations, Staff


# API Server
# Run this from the root directory with `uvicorn main:app --reload`
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/location/", response_model=LocationRead)
def create_location(location: LocationCreate):
    with Session(engine) as session:
        validLocation = Locations.model_validate(location)
        session.add(validLocation)
        session.commit()
        session.refresh(validLocation)
        return validLocation


@app.post("/staff/", response_model=Staff)
def create_staff(staff: Staff):
    with Session(engine) as session:
        validStaff = Staff.model_validate(staff)
        session.add(validStaff)
        session.commit()
        session.refresh(validStaff)
        return staff
