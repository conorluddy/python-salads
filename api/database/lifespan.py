from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from constants.config import SQLITE_URL

# Database Table definitions
# The noqa comment is used to ignore the F401 flake8 linting error
# which is raised when an imported module is not used, but we need
# to import here so that our tables will be created with SQLModel
from database.tables import (  # noqa: F401
    LocationsStaff,
    Locations,
    Staff,
    Roles,
    Menus,
    Recipes,
    Ingredients,
    Deliveries,
    DeliveriesIngredients,
    Orders,
    OrderItems,
    OrderItemsModifiers,
    OrderItemsAllergens,
    Modifiers,
    Allergens,
    StockAdjustments,
    StockAdjustmentsIngredients,
)


def create_db_and_tables():
    print("\nCreating SQLite database and creating tables \n")
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("\nClosing SQLite database connection - Bye!\n")


engine = create_engine(SQLITE_URL, echo=True)  # echo is for debugging, remove for prod
