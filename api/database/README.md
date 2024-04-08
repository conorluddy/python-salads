# Database 

Database related code lives in here

## Tables.py

This holds the definitions for tables. I'm using [SQLModel](https://sqlmodel.tiangolo.com/) for this because it seemed to be the quickest way to get set up with everything and works well with FastAPI.

## Seed

These are the API endpoints for seeding the database (they could have lived in the api/routes directory either but because they're meant as a single use endpoint I thought it would be cleaner to keep them away from the main routes). They provide an endpoint for each table that needs to be seeded, and a single seed-all endpoint that sequentially kicks them all off.

## Lifespan

This contains logic for initially creating the database, connecting to it, creating any intial tables if they don't exist yet, and closing everything when the server is shut down. 

## weirdsalads.db

This is our actual SQLite database, which is ignored in git but will be created if it doesn't already exist once the lifespan code is initiated.