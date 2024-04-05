from fastapi import APIRouter

ingredients_router = APIRouter()


@ingredients_router.get("/")
def get_all():
    return {"message": "Stub for get-all"}


@ingredients_router.get("/{id}")
async def get_by_id(id):
    return {"message": "Stub for get-by-id"}
