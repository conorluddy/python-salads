from sqlmodel import Session, select
from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database.tables import (
    Ingredients,
    OrderRecipeItem,
    Orders,
    Recipes,
    RecipesIngredients,
)
from database.lifespan import get_session

orders_router = APIRouter()


class OrderRequestRecipe(BaseModel):
    id: int


class OrderRequest(BaseModel):
    staff_id: int
    name: Optional[str]
    recipes: list[OrderRequestRecipe]


@orders_router.post("/")
def create_order(request: OrderRequest, session: Session = Depends(get_session)):

    # Create the Order as the base for the actual order ingredients
    order = Orders(
        staff_id=request.staff_id,
        name=request.name,
        ingredients=[],
    )

    # TODO: Should check that the staff actually exists here too

    # Commit the order so we can grab the ID
    session.add(order)
    session.commit()
    session.refresh(order)

    order_recipe_index = 0
    # Add each recipe once we verify it exists
    # (should also verify that there's enough ingredients available here,
    # although ideally that would be done upstream in the front-end first,
    # so that the recipe can never be added to the order to begin with)
    for request_recipe in request.recipes:
        recipe = session.get(Recipes, request_recipe.id)
        if recipe is None:
            print(f"Recipe {recipe.id} not found")
            continue

        # Create the order recipe relationship
        order_recipe = OrderRecipeItem(
            order_recipe_index=order_recipe_index,
            order_id=order.id,
            recipe_id=recipe.id,
        )

        # We need to differentiate between the same recipe being added multiple times
        order_recipe_index += 1

        # Reduce the ingredients in stock
        for recipe_ingredient in recipe.ingredients:

            ingredient = session.get(Ingredients, recipe_ingredient.id)
            if ingredient is None:
                print(f"Ingredient {recipe_ingredient.id} not found")
                continue

            # Get the quantity needed for this recipe from the junction table so we know how much to use
            ingredient_quantity = (
                session.exec(
                    select(RecipesIngredients).where(
                        RecipesIngredients.recipe_id == recipe.id,
                        RecipesIngredients.ingredient_id == recipe_ingredient.id,
                    )
                )
                .first()
                .ingredient_quantity
            )
            ingredient.units_in_stock -= ingredient_quantity
            session.add(ingredient)

        session.add(order_recipe)

    # if check everything was added correctly
    # return {"message": "Oops. Order not created."}

    session.commit()
    return {"message": "Order created."}
