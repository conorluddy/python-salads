from fastapi import APIRouter

staff_router = APIRouter()


@staff_router.get("/")
def get_all():
    return {"message": "Stub for get-all"}


@staff_router.get("/{id}")
async def get_by_id(id):
    return {"message": "Stub for get-by-id"}
