# Name and path for our SQLite database
SQLITE_PATH = "database/weirdsalads.db"
SQLITE_URL = f"sqlite:///{SQLITE_PATH}"

# A default password for the Staff members
DEFAULT_STAFF_PASSWORD = 1111

# The quantity of units of stock that any ingredient should start with when we seed the database
INITIAL_UNITS_IN_STOCK = 1000

# CORS whitelisting for our frontend-backend communication
ALLOWED_CORS_ORIGINS = ["http://localhost:3000"]


# A location ID that we'd probably put into a .env file instead.
# To be set for each branch of the restaurant when we're setting up a new system on-site.
# This is so that we can map the seed data to the correct location.
HARD_CODED_LOCATION_ID = 1
