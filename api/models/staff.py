from typing import List
from sqlmodel import SQLModel
from database.tables import Locations


class StaffCreate(SQLModel):
    id: int
    name: str
    dob: str
    iban: str
    bic: str
    locations: List["Locations"] = []


class StaffRead(SQLModel):
    id: int
    name: str
    dob: str
    iban: str
    bic: str
    locations: List["Locations"]
