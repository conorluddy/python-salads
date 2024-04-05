from fastapi import FastAPI
from database.seed import (
    seed_ingredients_from_csv,
    seed_locations_from_csv,
    seed_staff_from_csv,
)
from database.lifespan import lifespan


# API Server
# Run this from the root directory with `uvicorn main:app --reload`
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/seed/locations")
def seed_locations():
    seed_locations_from_csv()


@app.post("/seed/staff")
def seed_staff():
    seed_staff_from_csv()


@app.post("/seed/ingredients")
def seed_ingredients():
    seed_ingredients_from_csv()
