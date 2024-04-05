import csv
from sqlmodel import Session, select
from constants.config import HARD_CODED_LOCATION_ID
from database.lifespan import engine
from database.tables import Locations, Staff


def read_csv(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def seed_locations_from_csv():
    data = read_csv("data/locations.csv")
    with Session(engine) as session:
        has_locations = bool(session.exec(select(Locations)).first())
        if has_locations:
            return "The locations table has already been seeded."
        for location_data in data:
            # TODO: Make a type for the CSV data as their IDs keys arent "id"
            #  we're converting location_id to id here
            location_data["id"] = location_data.pop("location_id")
            location = Locations(**location_data)
            session.add(location)
        session.commit()
        return "Locations seeded."


def seed_staff_from_csv():
    data = read_csv("data/staff.csv")

    # We only want to seed staff that belong to this location,
    # so we filter the data based on the location_id
    staff_of_this_location = list(
        filter(lambda staff: int(staff["location_id"]) == HARD_CODED_LOCATION_ID, data)
    )

    with Session(engine) as session:
        has_existing_staff = bool(session.exec(select(Staff)).first())
        current_location = session.exec(select(Locations)).first()

        if has_existing_staff:
            return "The staff table has already been seeded."
        if current_location is None:
            return "Please seed the Locations table first"
        for staff_data in staff_of_this_location:
            staff_data["id"] = staff_data.pop("staff_id")
            staff = Staff(**staff_data)
            session.add(staff)

        session.commit()
        return "Staff seeded."
