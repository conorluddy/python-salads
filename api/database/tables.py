from datetime import datetime
from typing import List
from sqlmodel import Field, Relationship, SQLModel
from constants.config import DEFAULT_STAFF_PASSWORD
from models.units import UnitOfMeasurement


# Junction/Link Tables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# LocationsStaff -
# We don't really need this because we're only using one location per database
class LocationsStaff(SQLModel, table=True):
    location_id: int = Field(foreign_key="locations.id", primary_key=True)
    staff_id: int = Field(foreign_key="staff.id", primary_key=True)


# LocationsRecipes aka "Menus"
class LocationsRecipes(SQLModel, table=True):
    location_id: int = Field(foreign_key="locations.id", primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.id", primary_key=True)
    price: int  # I'm converting all monetary values to a cent based integer
    allow_allergens: bool
    allow_modifiers: bool


# RecipesIngredients - Joins Recipes and Ingredients
# with a quantity for the ingredient
class RecipesIngredients(SQLModel, table=True):
    recipe_id: int = Field(foreign_key="recipes.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredients.id", primary_key=True)
    ingredient_quantity: float  # How much of the ingredient is needed for the recipe


# DeliveriesIngredients
class DeliveriesIngredients(SQLModel, table=True):
    delivery_id: int = Field(foreign_key="deliveries.id", primary_key=True)
    ingredient_id: int = Field(foreign_key="ingredients.id", primary_key=True)
    ingredient_quantity: float


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
    email: str
    password: str = DEFAULT_STAFF_PASSWORD
    role: str  # TODO: Use the role enum here
    locations: List["Locations"] = Relationship(
        back_populates="staff", link_model=LocationsStaff
    )
    deliveries: List["Deliveries"] = Relationship(back_populates="staff")
    orders: List["Orders"] = Relationship(back_populates="staff")


# Recipes
class Recipes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    locations: List["Locations"] = Relationship(
        back_populates="recipes", link_model=LocationsRecipes
    )
    ingredients: List["Ingredients"] = Relationship(
        back_populates="recipes", link_model=RecipesIngredients
    )


# Ingredients
class Ingredients(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    unit: UnitOfMeasurement
    cost_per_unit: int  # I'm converting all monetary values to integers
    units_in_stock: float
    recipes: List["Recipes"] = Relationship(
        back_populates="ingredients", link_model=RecipesIngredients
    )
    deliveries: List["Deliveries"] = Relationship(
        back_populates="ingredients", link_model=DeliveriesIngredients
    )


# Deliveries
class Deliveries(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    staff: Staff = Relationship(back_populates="deliveries")
    staff_id: int = Field(default=None, foreign_key="staff.id")
    ingredients: List["Ingredients"] = Relationship(
        back_populates="deliveries", link_model=DeliveriesIngredients
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        # TODO: Handle timezones, set in config per restaurant
    )


# Orders
class Orders(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # Placeholder for maybe a customer name
    staff: Staff = Relationship(back_populates="orders")
    staff_id: int = Field(default=None, foreign_key="staff.id")
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        # TODO: Handle timezones, set in config per restaurant
    )


# OrderRecipeItem
# One row per recipe in an order
class OrderRecipeItem(SQLModel, table=True):
    order_id: int = Field(foreign_key="orders.id", primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.id", primary_key=True)
    order_recipe_index: int = Field(default=None, primary_key=True)
    # allergens: List["Allergens"] = Relationship(
    #     back_populates="order_recipe_items", link_model=OrderItemsAllergens
    # )
    # modifiers: List["Modifiers"] = Relationship(
    #     back_populates="order_recipe_items", link_model=OrderItemsModifiers
    # )


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
