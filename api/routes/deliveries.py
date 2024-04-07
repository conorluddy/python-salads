from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session
from pydantic import BaseModel
from database.tables import Deliveries, DeliveriesIngredients, Ingredients
from database.lifespan import get_session

deliveries_router = APIRouter()


class DeliveryRequestIngredient(BaseModel):
    id: int
    quantity: float


class DeliveryRequest(BaseModel):
    staff_id: int
    name: Optional[str]
    ingredients: list[DeliveryRequestIngredient]


@deliveries_router.post("/")
def deliver(request: DeliveryRequest, session: Session = Depends(get_session)):

    # Create the Delivery as the base for the actual delivery ingredients
    delivery = Deliveries(
        staff_id=request.staff_id,
        name=request.name,
        ingredients=[],
    )

    # Commit the delivery so we can grab the ID
    session.add(delivery)
    session.commit()
    session.refresh(delivery)

    # Add each ingredient once we find them in DB first
    for delivery_ingredient in request.ingredients:
        ingredient = session.get(Ingredients, delivery_ingredient.id)
        if ingredient is None:
            print(f"Ingredient {delivery_ingredient.id} not found")
            continue

        delivery_ingredient = DeliveriesIngredients(
            delivery_id=delivery.id,
            ingredient_id=ingredient.id,
            ingredient_quantity=delivery_ingredient.quantity,
        )
        session.add(delivery_ingredient)

    session.commit()
    return {"message": "Delivery delivered. 🚚"}
