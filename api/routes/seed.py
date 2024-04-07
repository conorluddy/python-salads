from fastapi import APIRouter

from database.seed import (
    seed_ingredients_from_csv,
    seed_locations_from_csv,
    seed_menus_from_csv,
    seed_recipes_from_csv,
    seed_staff_from_csv,
)

seed_router = APIRouter()


@seed_router.post("/")
def seed_all():
    """
    Seed all data.

    This endpoint seeds all the data including locations, staff, ingredients, recipes, and menus from CSV files.

    Returns:
        dict: A dictionary with a success message.
    """
    seed_locations_from_csv()
    seed_staff_from_csv()
    seed_ingredients_from_csv()
    seed_recipes_from_csv()
    seed_menus_from_csv()
    return {"message": "All data seeded successfully 🌱"}


@seed_router.post("/locations")
def seed_locations():
    """
    Seed locations.

    This endpoint seeds locations from a CSV file.

    Returns:
        dict: A dictionary with a success message.
    """
    return seed_locations_from_csv()


@seed_router.post("/staff")
def seed_staff():
    """
    Seed staff.

    This endpoint seeds staff from a CSV file.

    Returns:
        dict: A dictionary with a success message.
    """
    return seed_staff_from_csv()


@seed_router.post("/ingredients")
def seed_ingredients():
    """
    Seed ingredients.

    This endpoint seeds ingredients from a CSV file.

    Returns:
        dict: A dictionary with a success message.
    """
    return seed_ingredients_from_csv()


@seed_router.post("/recipes")
def seed_recipes():
    """
    Seed recipes.

    This endpoint seeds recipes from a CSV file.

    Returns:
        dict: A dictionary with a success message.
    """
    return seed_recipes_from_csv()


@seed_router.post("/menus")
def seed_menus():
    """
    Seed menus.

    This endpoint seeds menus from a CSV file.

    Returns:
        dict: A dictionary with a success message.
    """
    return seed_menus_from_csv()
