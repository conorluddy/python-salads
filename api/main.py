from fastapi import FastAPI
from database.seed import seed_locations_from_csv
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
