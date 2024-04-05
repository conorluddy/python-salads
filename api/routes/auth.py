from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Staff
from database.lifespan import engine
from pydantic import BaseModel

auth_router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


def get_session():
    with Session(engine) as session:
        yield session


@auth_router.post("/login")
def login(login_request: LoginRequest, session: Session = Depends(get_session)):
    staff = session.exec(
        select(Staff).where(
            Staff.email == login_request.email, Staff.password == login_request.password
        )
    ).first()
    if not staff:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return staff
