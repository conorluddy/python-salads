from fastapi import FastAPI
from database.lifespan import lifespan
from routes.ingredients import ingredients_router
from routes.locations import locations_router
from routes.menus import menus_router
from routes.recipes import recipes_router
from routes.seed import seed_router
from routes.staff import staff_router


# API Server
# Run this from the root directory with `uvicorn main:app --reload`
app = FastAPI(lifespan=lifespan)

# Routers - TODO: Move these to a separate location/function
app.include_router(ingredients_router, prefix="/ingredients")
app.include_router(locations_router, prefix="/locations")
app.include_router(menus_router, prefix="/menus")
app.include_router(recipes_router, prefix="/recipes")
app.include_router(staff_router, prefix="/staff")
app.include_router(seed_router, prefix="/seed")
