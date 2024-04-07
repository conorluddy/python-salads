from enum import Enum

# These are used by the Ingredients table
# to enforce the strings that we would seed for the unit of measurement.


class UnitOfMeasurement(Enum):
    centiliter = "centiliter"
    deciliter = "deciliter"
    liter = "liter"
    milliliter = "milliliter"
