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
    seed_locations_from_csv()
    seed_staff_from_csv()
    seed_ingredients_from_csv()
    seed_recipes_from_csv()
    seed_menus_from_csv()
    return {"message": "All data seeded successfully 🌱"}


@seed_router.post("/locations")
def seed_locations():
    return seed_locations_from_csv()


@seed_router.post("/staff")
def seed_staff():
    return seed_staff_from_csv()


@seed_router.post("/ingredients")
def seed_ingredients():
    return seed_ingredients_from_csv()


@seed_router.post("/recipes")
def seed_recipes():
    return seed_recipes_from_csv()


@seed_router.post("/menus")
def seed_menus():
    return seed_menus_from_csv()
