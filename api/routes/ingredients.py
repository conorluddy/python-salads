from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Ingredients
from database.lifespan import engine

ingredients_router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@ingredients_router.get("/")
def get_all(session: Session = Depends(get_session)):
    ingredients = session.exec(select(Ingredients)).all()
    return ingredients


@ingredients_router.get("/{ingredient_id}")
def get_by_id(ingredient_id: int, session: Session = Depends(get_session)):
    ingredient = session.get(Ingredients, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient
