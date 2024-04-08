from enum import Enum

# I was intending to use these like how you would in Typscript,
# to enforce the strings that we would seed for the staff roles,
# but it didn't work as expected and I hadn't enough time to dig into it.


class Role(Enum):
    BOH = "Back-of-house"
    CHEF = "Chef"
    FOH = "Front-of-house"
    MANAGER = "Manager"
