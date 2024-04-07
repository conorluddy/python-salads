from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Ingredients
from database.lifespan import engine

ingredients_router = APIRouter()


def get_session():
    """
    Function to create a new session with the database engine.
    """
    with Session(engine) as session:
        yield session


@ingredients_router.get("/")
def get_all(session: Session = Depends(get_session)):
    """
    Retrieve all ingredients from the database.

    Returns:
    - List of all ingredients.
    """
    ingredients = session.exec(select(Ingredients)).all()
    return ingredients


@ingredients_router.get("/{ingredient_id}")
def get_by_id(ingredient_id: int, session: Session = Depends(get_session)):
    """
    Retrieve an ingredient by its ID from the database.

    Parameters:
    - ingredient_id: The ID of the ingredient.

    Returns:
    - The ingredient with the specified ID.

    Raises:
    - HTTPException 404: If the ingredient is not found.
    """
    ingredient = session.get(Ingredients, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient
