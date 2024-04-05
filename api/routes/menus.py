from fastapi import APIRouter

menus_router = APIRouter()


@menus_router.get("/")
def get_all():
    return {"message": "Stub for get-all"}


@menus_router.get("/{id}")
async def get_by_id(id):
    return {"message": "Stub for get-by-id"}
