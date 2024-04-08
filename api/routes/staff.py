from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.tables import Staff
from database.lifespan import get_session

staff_router = APIRouter()


@staff_router.get("/")
def get_all(session: Session = Depends(get_session)):
    """
    Endpoint to get all staff members.

    Returns:
        List[Staff]: A list of all staff members.
    """
    staff = session.exec(select(Staff)).all()
    return staff


@staff_router.get("/{staff_id}")
def get_by_id(staff_id: int, session: Session = Depends(get_session)):
    """
    Endpoint to get a staff member by their ID.

    Args:
        staff_id (int): The ID of the staff member.

    Returns:
        Staff: The staff member with the specified ID.

    Raises:
        HTTPException: If the staff member is not found.
    """
    staff = session.get(Staff, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff
