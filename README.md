
# Weird Salad!

A technical challenge about weird salads

## Table of Contents

- [Weird Salad!](#weird-salad)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation and local development](#installation-and-local-development)
    - [Front end](#front-end)
      - [Install dependencies](#install-dependencies)
      - [Run in development](#run-in-development)
      - [Run in production](#run-in-production)
  - [Usage](#usage)
  - [Design/Development decisions](#designdevelopment-decisions)
  - [Git Strategy](#git-strategy)
  - [Testing](#testing)
  - [Entity Relationships](#entity-relationships)
  - [Future plans](#future-plans)

## Overview

This is a full stack project, far from complete, for a basic inventory management application for a fictional salad restaurant chain. The time limit was supposed to be around 4-5 hours, but I've used the full day. I would gladly spend more time building this out, but I do understand that the aim of the assignment is to prioritise certain parts of the spec, and not expect to complete it.

I'm using Python for the back end, with [FastAPI](https://fastapi.tiangolo.com/) for building out the API endpoints. [SQLModel](https://sqlmodel.tiangolo.com/) paired nicely with it for setting up the database tables and relationships. The database is stored in SQLite.

The frontend uses [NextJS](https://nextjs.org/) 14 to allowing for rapid creation of a single page application with routing and data fetching. I used [MaterialUI](https://mui.com/material-ui/all-components/) just to let me fire components together real quick.

I used [Miro](https://miro.com/) to roughly sketch out the entity relationships - you can see that diagram below.


## Project Structure

Everything for the backend is under the [/api](https://github.com/conorluddy/python-salads/tree/develop/api) directory
Everything for the frontend is under the [/client](https://github.com/conorluddy/python-salads/tree/develop/api) directory

## Installation

### Prerequisites

- **Python**: Ensure Python is installed on the system. It’s recommended to use the latest version unless the project specifies otherwise. You can download Python from [python.org](https://www.python.org/).
- **pip**: Ensure pip (Python package installer) is installed. It usually comes with Python.

### Installation and local development 

**Clone the Repository**

Clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/conorluddy/python-salads
```


**Back end**

CD into the directory for the API part of the application *(Not the project root)*

```bash
cd python-salads/api
```

Set up a virtual environment for Python

```bash
python3 -m venv venv
```

Active the virtual environment 

```bash
# OSX
source venv\Scripts\activate
# Windows
venv\Scripts\activate
```


Install the dependencies
```bash
pip install -r requirements.txt
```

Run the server with the following command, it will create any database tables that don't already exist, so you may need to scroll back up to see the served URL, but it should be up and running on `http://127.0.0.1:8000`

```bash
uvicorn main:app --reload
```

https://github.com/conorluddy/python-salads/blob/documentation/documentation/assets/api-install.mp4

**Seeding the database**

Once the API being served, you can check out the [Swagger docs for the available endpoints](http://127.0.0.1:8000/docs) here.

To initially populate the database from the data provided with the assignment you'll need to POST to the seed endpoint, you can [trigger that via the swagger docs here](http://127.0.0.1:8000/docs#/Database%20Seeding/seed_all_seed__post)

This imports data from the CSV files under `api/data` and stores it. Once there's data in the database you should be able to hit the other GET endpoints listed in the Swagger docs and see your data. The available endpoints are as far as I got with the API side of this assignment before I decided that I should build a basic front-end, so that we would at least have a full end-to-end flow.

![Seeding the database](https://github.com/conorluddy/python-salads/blob/develop/documentation/assets/Seeding.png)

### Front end

CD into the /client directory (in a separate terminal, so we can run this in parallel to the API)

```bash
cd python-salads/client
```

#### Install dependencies

```bash
npm install
```

#### Run in development

```bash
npm run dev
```

#### Run in production

First we need to `build` it

```bash
npm run build
```

Then we can `start` it.

```bash
npm start
```

## Usage



## Design/Development decisions

> Just like with the spreadsheets before, each location has its own data. The application will run on a computer in-store, which could be running any of Windows, macOS or Linux. The app will not be public facing, it should not be shared across locations. Each site has secure Wi-Fi and staff will access the store’s system using a mobile web browser via a local IP address.

## Git Strategy

## Testing

## Entity Relationships
![Database entity relationship diagram](https://github.com/conorluddy/python-salads/blob/documentation/documentation/assets/ERD.png)

## Future plans