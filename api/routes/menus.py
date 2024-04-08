from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import LocationsRecipes
from database.lifespan import get_session

menus_router = APIRouter()


@menus_router.get("/")
def get_all(session: Session = Depends(get_session)):
    """
    Get all menus.

    Returns:
        List[LocationsRecipes]: A list of all menus.
    """
    menus = session.exec(select(LocationsRecipes)).all()
    return menus


@menus_router.get("/{menu_id}")
def get_by_id(menu_id: int, session: Session = Depends(get_session)):
    """
    Get a menu by its ID.

    Args:
        menu_id (int): The ID of the menu.

    Returns:
        LocationsRecipes: The menu with the specified ID.

    Raises:
        HTTPException: If the menu with the specified ID is not found.
    """
    menu = session.get(LocationsRecipes, menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu
