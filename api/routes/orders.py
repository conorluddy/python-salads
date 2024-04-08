from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session
from pydantic import BaseModel

from database.tables import OrderRecipeItem, Orders, Recipes
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
        # TODO ...

        session.add(order_recipe)

    # if check everything was added correctly
    # return {"message": "Oops. Order not created."}

    session.commit()
    return {"message": "Order created."}
