import csv
import re
from sqlmodel import Session, select
from constants.config import HARD_CODED_LOCATION_ID, INITIAL_UNITS_IN_STOCK
from database.lifespan import engine
from database.tables import (
    Ingredients,
    Locations,
    LocationsRecipes,
    Recipes,
    RecipesIngredients,
    Staff,
)
from utilities.numbers import parse_cost_to_cents


def read_csv(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def seed_locations_from_csv():
    data = read_csv("data/locations.csv")
    with Session(engine) as session:
        has_locations = bool(session.exec(select(Locations)).first())
        if has_locations:
            return "The locations table has already been seeded."
        for location_data in data:
            # TODO: Make a type for the CSV data as their IDs keys arent "id"
            #  we're converting location_id to id here
            location_data["id"] = location_data.pop("location_id")
            location = Locations(**location_data)
            session.add(location)
        session.commit()
        return "Locations seeded."  # TODO: Return the number of locations seeded


def seed_staff_from_csv():
    data = read_csv("data/staff.csv")

    # We only want to seed staff that belong to this location,
    # so we filter the data based on the location_id
    staff_of_this_location = list(
        filter(lambda staff: int(staff["location_id"]) == HARD_CODED_LOCATION_ID, data)
    )

    with Session(engine) as session:
        has_existing_staff = bool(session.exec(select(Staff)).first())
        current_location = session.exec(select(Locations)).first()

        if has_existing_staff:
            return "The staff table has already been seeded."
        if current_location is None:
            return "Please seed the Locations table first"
        for staff_data in staff_of_this_location:
            staff_data["id"] = staff_data.pop("staff_id")
            staff_data["email"] = (
                re.sub(r"\s+", ".", re.sub(r"[^\w\s]", "", staff_data["name"])).lower()
                + "@weirdsalads.com"
            )
            staff = Staff(**staff_data)
            session.add(staff)

        session.commit()
        return "Staff seeded."  # TODO: give more info on the number of staff seeded


def seed_ingredients_from_csv():
    data = read_csv("data/ingredients.csv")

    with Session(engine) as session:
        has_been_seeded = bool(session.exec(select(Ingredients)).first())

        if has_been_seeded:
            return "The ingredients have already been seeded. Pun intended."

        for ingredient_data in data:
            ingredient_data["id"] = ingredient_data.pop("ingredient_id")

            # We're setting the initial stock level here.
            # We could set it as zero and wait for a delivery, but will use 1000 for now
            ingredient_data["units_in_stock"] = INITIAL_UNITS_IN_STOCK

            # I'm converting the cost to cents here, similar to how Stripe
            # use cent based numbers rather than floating point
            cost_string = ingredient_data.pop("cost")
            ingredient_data["cost_per_unit"] = parse_cost_to_cents(cost_string)

            ingredient = Ingredients(**ingredient_data)
            session.add(ingredient)

        session.commit()
        return "Ingredients seeded."


def seed_recipes_from_csv():
    data = read_csv("data/recipes.csv")
    with Session(engine) as session:
        for recipe_data in data:
            # Create/fetch the recipe
            recipe = session.get(Recipes, recipe_data["recipe_id"])
            if recipe is None:
                recipe = Recipes(id=recipe_data["recipe_id"], name=recipe_data["name"])
                session.add(recipe)

            # Create the relationship
            ingredient = session.get(Ingredients, recipe_data["ingredient_id"])
            if ingredient is None:
                # Handle missing ingredient
                continue

            # RecipeIngredients instance
            recipe_ingredient = RecipesIngredients(
                recipe_id=recipe.id,
                ingredient_id=ingredient.id,
                ingredient_quantity=float(recipe_data["quantity"]),
            )
            session.add(recipe_ingredient)

        session.commit()
        return "Recipes seeded."


def seed_menus_from_csv():
    data = read_csv("data/menus.csv")
    with Session(engine) as session:
        for menu_data in data:
            # Filter for the current location
            if int(menu_data["location_id"]) != HARD_CODED_LOCATION_ID:
                continue

            # Fetch the recipe if it exists already in the sesh
            recipe = session.get(Recipes, menu_data["recipe_id"])
            if recipe is None:
                continue

            # Check if the menu item already exists
            existing_menu_item = session.exec(
                select(LocationsRecipes).where(
                    LocationsRecipes.location_id == HARD_CODED_LOCATION_ID,
                    LocationsRecipes.recipe_id == recipe.id,
                )
            ).first()

            if existing_menu_item:
                continue

            # If no existing menu item, create a new one
            menu_item = LocationsRecipes(
                location_id=HARD_CODED_LOCATION_ID,
                recipe_id=recipe.id,
                price=parse_cost_to_cents(menu_data["price"]),
                # Lets leave modifiers til V2...
                # I'm aliasing modifiers to separate allergens from recipe extras
                allow_modifiers=False,  # menu_data["modifiers"] == "1",
                allow_allergens=False,  # menu_data["modifiers"] == "2",
            )
            session.add(menu_item)

        session.commit()
        return "Menus seeded."
