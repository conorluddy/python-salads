from fastapi import FastAPI
from database.lifespan import lifespan
from routes.seed import seed_router


# API Server
# Run this from the root directory with `uvicorn main:app --reload`
app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(seed_router, prefix="/seed", tags=["Seeding"])
