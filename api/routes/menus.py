from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import LocationsRecipes
from database.lifespan import engine

menus_router = APIRouter()

# TODO: This is quick and dirty but there'll be confusion here between LocationsRecipes and Menus - clear up ambiguity


def get_session():
    with Session(engine) as session:
        yield session


@menus_router.get("/")
def get_all(session: Session = Depends(get_session)):
    menus = session.exec(select(LocationsRecipes)).all()
    return menus


@menus_router.get("/{menu_id}")
def get_by_id(menu_id: int, session: Session = Depends(get_session)):
    menu = session.get(LocationsRecipes, menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu
