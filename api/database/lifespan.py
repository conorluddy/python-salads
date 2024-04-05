from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from constants.config import SQLITE_URL


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("\nClosing SQLite database connection\n")


def create_db_and_tables():
    print("\nCreating SQLite database and creating tables - Bye! \n")
    SQLModel.metadata.create_all(engine)


engine = create_engine(SQLITE_URL, echo=True)  # echo is for debugging, remove for prod
