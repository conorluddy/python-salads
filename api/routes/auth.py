from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Staff
from database.lifespan import engine

auth_router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@auth_router.post("/login")
def login(email: str, password: str, session: Session = Depends(get_session)):
    staff = session.exec(
        select(Staff).where(Staff.email == email, Staff.password == password)
    ).first()
    if not staff:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return staff
