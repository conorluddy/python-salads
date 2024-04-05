from sqlmodel import Field, SQLModel


# LocationsStaff ~~~~~~~~~~~~~~~~~~~~~


class LocationsStaff(SQLModel, table=True):
    location_id: int = Field(foreign_key="locations.id", primary_key=True)
    staff_id: int = Field(foreign_key="staff.id", primary_key=True)


# Locations ~~~~~~~~~~~~~~~~~~~~~


class Locations(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(index=True)


# Staff ~~~~~~~~~~~~~~~~~~~~~


class Staff(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(index=True)


# Roles ~~~~~~~~~~~~~~~~~~~~~


class Roles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)


# Menus ~~~~~~~~~~~~~~~~~~~~~


class Menus(SQLModel, table=True):
    location_id: int = Field(foreign_key="locations.id", primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.id", primary_key=True)


# Recipes ~~~~~~~~~~~~~~~~~~~~~


class Recipes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)


# Ingredients ~~~~~~~~~~~~~~~~~~~~~


class Ingredients(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)


# Deliveries ~~~~~~~~~~~~~~~~~~~~~


class Deliveries(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)


# DeliveriesIngredients ~~~~~~~~~~~~~~~~~~~~~


class DeliveriesIngredients(SQLModel, table=True):
    deliveries_id: int = Field(foreign_key="locations.id", primary_key=True)
    ingredients_id: int = Field(foreign_key="ingredients.id", primary_key=True)


# Orders ~~~~~~~~~~~~~~~~~~~~~


class Orders(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# OrderItems ~~~~~~~~~~~~~~~~~~~~~


class OrderItems(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# OrderItemsModifiers ~~~~~~~~~~~~~~~~~~~~~


class OrderItemsModifiers(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# OrderItemsAllergens ~~~~~~~~~~~~~~~~~~~~~


class OrderItemsAllergens(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# Modifiers ~~~~~~~~~~~~~~~~~~~~~


class Modifiers(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# Allergens ~~~~~~~~~~~~~~~~~~~~~


class Allergens(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# StockAdjustments ~~~~~~~~~~~~~~~~~~~~~


class StockAdjustments(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


# StockAdjustmentsIngredients ~~~~~~~~~~~~~~~~~~~~~


class StockAdjustmentsIngredients(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
