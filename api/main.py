from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from constants.config import ALLOWED_CORS_ORIGINS
from database.lifespan import lifespan
from routes.ingredients import ingredients_router
from routes.locations import locations_router
from routes.menus import menus_router
from routes.recipes import recipes_router
from routes.seed import seed_router
from routes.staff import staff_router


# API Server-  Run with `uvicorn main:app --reload`
app = FastAPI(lifespan=lifespan)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(locations_router, prefix="/locations", tags=["Locations"])
app.include_router(staff_router, prefix="/staff", tags=["Staff"])
app.include_router(menus_router, prefix="/menus", tags=["Menus"])
app.include_router(recipes_router, prefix="/recipes", tags=["Recipes"])
app.include_router(ingredients_router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(seed_router, prefix="/seed", tags=["Database Seeding"])
