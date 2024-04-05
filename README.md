
# Weird Salad!

A technical challenge about weird salads

## Table of Contents

- [Weird Salad!](#weird-salad)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installation and locel development steps](#installation-and-locel-development-steps)
    - [Back end](#back-end)
    - [Front end](#front-end)
  - [Usage](#usage)
  - [Git Strategy](#git-strategy)
  - [Testing](#testing)
  - [Entity Relationships](#entity-relationships)
  - [Future plans](#future-plans)

## Overview

This is a full stack project, far from complete, for a basic inventory management application for a fictional salad restaurant chain. The time limit was supposed to be around 4-5 hours, but I've used the full day.

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

### Installation and locel development steps

**Clone the Repository**

Clone the project repository from GitHub to your local machine.

```bash
git clone https://github.com/conorluddy/python-salads
```


### Back end

CD into the directory for the API part of the application *(Not the project root)*

```bash
cd python-salads/api
```

Set up a virtual environment for Python

```bash
python3 -m venv venv
```

Active the virtual environment 

OSX
```bash
source venv\Scripts\activate
```

Windows
```bash
venv\Scripts\activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run the server
```bash
uvicorn main:app --reload
```

### Front end

CD into the /client directory
```bash
cd python-salads/client
```

Install dependencies
```bash
npm install
```

Run it!
```bash
npm run dev
```


## Usage

## Git Strategy

## Testing

## Entity Relationships
![Database entity relationship diagram](https://github.com/conorluddy/python-salads/blob/documentation/documentation/assets/ERD.png)

## Future plans