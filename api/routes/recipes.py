from fastapi import APIRouter

recipes_router = APIRouter()


@recipes_router.get("/")
def get_all():
    return {"message": "Stub for get-all"}


@recipes_router.get("/{id}")
async def get_by_id(id):
    return {"message": "Stub for get-by-id"}
