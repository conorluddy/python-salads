
# Weird Salad!

A technical challenge about weird salads.

*Please note*: I built the bulk of this over the day on Friday 5th April and committed [this sha](https://github.com/conorluddy/python-salads/commit/d5eacee3f113f95faf76c6b3671898a275e316c5) at 17:33 on same. I did continue to throw together some rough documentation after that deadline, and completed additional endpoints for creating Delivery and Order instances over the weekend, however I'm well aware that I was supposed to drop this at the deadline time, so feel free to ignore anything that wasn't completed by then.

Although the front-end is very very bare at the moment, front-end and React is actually my strong side, so I may have wasted that by spending too much time on the back-end. There's an endless amount of additional work we could do on this, on both the back-end and the front-end, and it's quite an interesting coding challenge in that you never feel comfortable to hand it in - because it's never really complete! 

But I learned a lot in building this out, so thank you for the opportunity.

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
    - [On-site](#on-site)
  - [Git Strategy](#git-strategy)
  - [Design/Development decisions](#designdevelopment-decisions)
    - [Python](#python)
    - [FastAPI](#fastapi)
    - [SQLite](#sqlite)
    - [NextJS](#nextjs)
  - [Entity Relationships](#entity-relationships)
  - [Stuff I left out](#stuff-i-left-out)
  - [Other technical pitfalls](#other-technical-pitfalls)
    - [Dates, times and timezones](#dates-times-and-timezones)
  - [Future plans](#future-plans)
    - [PWA - Progressive Web App](#pwa---progressive-web-app)
    - [Storing customer data](#storing-customer-data)
  - [Testing](#testing)

## Overview

This is a full stack project, far from complete, for a basic inventory management application for a fictional salad restaurant chain. The time limit was supposed to be around 4-5 hours, but I've used the full day. I would gladly spend more time building this out, but I do understand that the aim of the assignment is to prioritise certain parts of the spec, and not expect to complete it.

**Please note: Everything that was built here so far was built with the aim of getting an MVP in front of a user which could be used to demo or provide some actual value and show an end-to-end flow. It's choc full of shortcuts, incomplete features, insecure data practices, and completely devoid of any form of testing!**

I'm using Python for the back end, with [FastAPI](https://fastapi.tiangolo.com/) for building out the API endpoints. [SQLModel](https://sqlmodel.tiangolo.com/) paired nicely with it for setting up the database tables and relationships. The database is currently SQLite (and this suits the spec where the app only needs to be running on-site).

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

Alternatively you could play around with this in [Postman](https://www.postman.com/downloads/), but FastAPI has Swagger built in by default, which is super handy.

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

With the API and the Client both running, you should be able to [navigate to the React app](http://localhost:3000/) on your localhost.

![Login page](https://github.com/conorluddy/python-salads/blob/develop/documentation/assets/login.png)

We don't have real authentication working here, I'll go into detail on that later in the docs, but if your database has been seeded it will have generated fake email addresses for each of the staff members, firstname.lastname@weirdsalads.com, and assigned them all a password of 1111. You can use the one hinted on the login page, assuming that the seeding has correctly populated the database.

When you log in, we just pass the email and password to the API. Passwords are not encrypted (gaping security hole), and if there's a match the API will return the entire Staff object in a blob of JSON (another GAPING security hole!). That data gets stored in sessionStorage in the FE, where it's then used as a pseudo "authorised" state. If there's a user saved in sessionStorage then you're assumed logged-in, and can access all of the things. In fact you could just manually add anything to sessionStorage under the 'staff' key and you'll get in.

Once logged in you'll see a Dashboard with some nav icons in the footer. I'd love to have had time to visually design all of this properly, but for now I just fired it together with MaterialUI

![dashboard](https://github.com/conorluddy/python-salads/blob/develop/documentation/assets/dashboard.png)

You can navigate around and log out afterwards.

![inventory](https://github.com/conorluddy/python-salads/blob/develop/documentation/assets/inventory.png)

![point of sales](https://github.com/conorluddy/python-salads/blob/develop/documentation/assets/pos.png)

### On-site

In a production environment when setting this up on-site for an actual branch of Weird Salads, we would need to un hard-code the Location ID. We could have a CLI tool for the initial setup, or manage it via an initial setup flow in the React app, where the installation engineer would set the correct LocationID in a .env file or path variable, or even just in the database by seeding it with a specific LocationID.

## Git Strategy

I set this repo up with a `main` branch intended as "production" and a `develop` branch as a primary branch to build features against. Feature branches are opened as PRs against `develop`, and `develop` would be merged into `main` whenever a fresh release to prod is ready to go. This works well on teams, where the feature branches are peer reviewed and need an approval before being merged into the primary branch. I was working fast and loose on this, but normally in a professional setting you would want to have PR templates to fill out details of what each PR contains. You would also want to set up a CI/CD pipeline with Github actions or Jenkins or similar, checking that tests pass before allowing anything to be merged to the core branches. Merges to `develop` or `main` would kick off a deployment build and push the built code out to the cloud. Feature branches and/or PRs can also be set up to provide preview environments for QA and end to end testing. AWS Amplify and Vercel are some nice examples of services that provide this kind of branch integration.


## Design/Development decisions

Why I made various tech choices in this repo.

### Python

I've wanted to learn and use more Python for a while now, partially because of it's applications in the fields of AI and machine learning, but also to have more server side applicable experience. The job spec for this role also specifies that it involves Python, so it made sense to jump straight in.

### FastAPI

As with Python above, it's part of the stack used in this role so it made sense to try it out. In retrospect I would have been much quicker in throwing something together in Node and Typescript, where I'm quickest and most comfortable, but this was a great learning experience regardless of the outcome.

### SQLite

From the technical spec for this assignment:

> ...each location has its own data. The application will run on a computer in-store, which could be running any of Windows, macOS or Linux. The app will not be public facing, it should not be shared across locations. Each site has secure Wi-Fi and staff will access the store’s system using a mobile web browser via a local IP address.

SQLite is a superbly capable database solution, particularly when we're only dealing with a single server instance for an in-house computer. We could run this whole system on a RaspberryPi and not need to worry about running out of resources. SQLite stores everything in one file, removing any need for additional database servers etc. 

In future when Weird Salads scales up, we would be able to migrate (albiet with some minor transformations), each restaurants data into a larger centralised PostgreSQL or similar system on a cloud provider. 

### NextJS

I only had a couple of hours left to work on a front-end for this application, and Next comes with a ton of functionality out of the box, allowing me to quickly stub out some routes for the MVP version of this app. In the longer term, Next 14 now has server components, which means that you can fetch data from the server rather than the users browser, exposing less detail about your API and allowing your Next application to cache data and generate static pages for data that doesn't change very often. Many of the tables we used in this app contain data that never changes (staff, reciepes etc). Even in a real world application, much of this data would be relatively static for days and weeks at a time. Next can be leveraged in such a way that components and pages using this data can be statically generated, so the database and API doesn't even need to get hit for them. When something *does*  change in the database, you can trigger [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration) to tell Next to rebuild any static components that need to fetch updated data. 

## Entity Relationships

I found that digging into the spreadsheet data and mapping all of this out in Miro actually ate a large chunk of time too, but it was quite enjoyable, and I'm sure there are errors in it. The lines joining the tables are likely not all correct in terms of the relationship cardinality, one-to-one, one-to-many etc etc.

I had intended that most of the data that gets seeded, never changes, so those tables are regarded as "static", wheras the stock levels and the tracking of who-changed-what would be changing constantly. Ideally we would be writing to those Orders, Deliveries and Stock Adjustments tables actively, and changes to them would trigger updates to the units_in_stock column of the Ingredients table.

When it came to generating reports we would be able to deduct from these table entries, exactly why, when and by whom the stock levels changed. 

![Database entity relationship diagram](https://github.com/conorluddy/python-salads/blob/develop/documentation/assets/ERD.png)

## Stuff I left out

Let me come back to this one, it's a big one...



## Other technical pitfalls

### Dates, times and timezones

Dates are hard. The data for the Weird Salads restaurant locations have postcodes across the USA. When this app does need to scale up and centralise all of their data, it will need to take into account that different locations will open and close at different times. Additionally, if some of them open into the night, or maybe open at 8pm and close at 4am, then it can introduce all sorts of complications when dealing with generating reports or managing stock.

## Future plans

Things that would be nice to add to this.

- The front-end is obviously completely incomplete, so that would need priority. We should now be able to take orders and deliveries. We need some more endpoints for reporting etc.
- Testing across frontend and backend.
- CI/CD
- This list could be endless :) 


### PWA - Progressive Web App

We could set the frontend up as a PWA so that it can be installed as an "app" on the devices in the restaurant. This appears to require a HTTPS cert for the server though, so goes a bit beyond what we have here with just serving the app from an in store IP address. But it would be a nice feature because it makes the frontend look like a native application, and gives you an app icon on your device.

### Storing customer data

We could take the customers name and phone or email when they're ordering, so that we can build up a database of customers to be used for marketing/discounts/etc. 

## Testing

Testing, as per usual when timelines are super tight, was ommitted. However I'm a big fan of testing and it has saved me and teams I've worked on some serious headaches over the years. 
You would absolutely want frontend and backend tests on this application if it was in use in a real restaurant. Ideally in a CI/CD pipeline so that new features can be regression tested so that they break as little as possible.