from typing import List
from sqlmodel import Field, Relationship, SQLModel

from models.roles import Role
from models.units import UnitOfMeasurement


# Junction/Link Tables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# LocationsStaff
class LocationsStaff(SQLModel, table=True):
    location_id: int = Field(foreign_key="locations.id", primary_key=True)
    staff_id: int = Field(foreign_key="staff.id", primary_key=True)


# LocationsRecipes aka "Menus"
class LocationsRecipes(SQLModel, table=True):
    location_id: int = Field(foreign_key="locations.id", primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.id", primary_key=True)
    price: int
    allow_allergens: bool
    allow_modifiers: bool


class RecipesIngredients(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="locations.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="recipes.id", primary_key=True)
    quantity: float


# Main Tables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Locations
class Locations(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    address: str
    staff: List["Staff"] = Relationship(
        back_populates="locations", link_model=LocationsStaff
    )
    recipes: List["Recipes"] = Relationship(
        back_populates="locations", link_model=LocationsRecipes
    )


# Staff
class Staff(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    dob: str
    iban: str
    bic: str
    role: Role
    locations: List["Locations"] = Relationship(
        back_populates="staff", link_model=LocationsStaff
    )


# Recipes
class Recipes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    locations: List["Locations"] = Relationship(
        back_populates="recipes", link_model=LocationsRecipes
    )
    # ingredients: List["Ingredients"] = Relationship(
    #     back_populates="recipes", link_model=RecipesIngredients
    # )


# Ingredients
class Ingredients(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    unit: UnitOfMeasurement
    cost_per_unit: int
    units_in_stock: float
    # recipes: List["Recipes"] = Relationship(
    #     back_populates="ingredients", link_model=RecipesIngredients
    # )


# Deliveries
class Deliveries(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)


# DeliveriesIngredients
class DeliveriesIngredients(SQLModel, table=True):
    deliveries_id: int = Field(foreign_key="locations.id", primary_key=True)
    ingredients_id: int = Field(foreign_key="ingredients.id", primary_key=True)


# Orders
class Orders(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# OrderItems
class OrderItems(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# OrderItemsModifiers
class OrderItemsModifiers(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# OrderItemsAllergens
class OrderItemsAllergens(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# Modifiers
class Modifiers(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# Allergens
class Allergens(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# StockAdjustments
class StockAdjustments(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# StockAdjustmentsIngredients
class StockAdjustmentsIngredients(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
