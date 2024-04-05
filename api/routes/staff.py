from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Staff
from database.lifespan import engine

staff_router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@staff_router.get("/")
def get_all(session: Session = Depends(get_session)):
    staff = session.exec(select(Staff)).all()
    return staff


@staff_router.get("/{staff_id}")
def get_by_id(staff_id: int, session: Session = Depends(get_session)):
    staff = session.get(Staff, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff
