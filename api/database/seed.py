import csv
from sqlmodel import Session, select
from database.lifespan import engine
from database.tables import Locations


def read_csv(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def seed_locations_from_csv():
    data = read_csv("data/locations.csv")
    with Session(engine) as session:
        has_locations = bool(session.exec(select(Locations)).first())
        if has_locations:
            print("The locations table is not empty. Seeding skipped.")
            return "The locations table is already seeded."
        for location_data in data:
            # TODO: Make a type for the CSV data as their IDs keys arent "id"
            #  we're converting location_id to id here
            location_data["id"] = location_data.pop("location_id")
            location = Locations(**location_data)
            session.add(location)
        session.commit()
        session.refresh(location)
        return "Locations seeded."
