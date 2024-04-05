from typing import List
from sqlmodel import SQLModel
from database.tables import Staff


class LocationCreate(SQLModel):
    id: int
    name: str
    address: str
    staff: List["Staff"] = []


class LocationRead(SQLModel):
    id: int
    name: str
    address: str
