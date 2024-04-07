from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Recipes
from database.lifespan import engine

recipes_router = APIRouter()


def get_session():
    """
    Get a database session using the engine.

    Returns:
        Session: The database session.
    """
    with Session(engine) as session:
        yield session


@recipes_router.get("/")
def get_all(session: Session = Depends(get_session)):
    """
    Get all recipes.

    Returns:
        List[Recipes]: A list of all recipes.
    """
    recipes = session.exec(select(Recipes)).all()
    return recipes


@recipes_router.get("/{recipe_id}")
def get_by_id(recipe_id: int, session: Session = Depends(get_session)):
    """
    Get a recipe by its ID.

    Args:
        recipe_id (int): The ID of the recipe.

    Returns:
        Recipes: The recipe with the specified ID.

    Raises:
        HTTPException: If the recipe is not found.
    """
    recipe = session.get(Recipes, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
