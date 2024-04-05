from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Recipes
from database.lifespan import engine

recipes_router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@recipes_router.get("/")
def get_all(session: Session = Depends(get_session)):
    recipes = session.exec(select(Recipes)).all()
    return recipes


@recipes_router.get("/{recipe_id}")
def get_by_id(recipe_id: int, session: Session = Depends(get_session)):
    recipe = session.get(Recipes, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
