from fastapi import APIRouter

locations_router = APIRouter()


@locations_router.get("/")
def get_all():
    return {"message": "Stub for get-all"}


@locations_router.get("/{id}")
async def get_by_id(id):
    return {"message": "Stub for get-by-id"}
