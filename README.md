# ComplimentAPI

This is a fun and simple API built using FastAPI, that allows you to create, read, update, delete, and randomly receive compliments! 

## Features
- `POST /compliments/` – Add a new compliment
- `GET /compliments/` – Retrieve a list of all compliments
- `GET /compliments/random` – Get a random compliment
- `PUT /compliments/{id}` – Update a compliment by ID
- `DELETE /compliments/{id}` – Delete a compliment by ID


##  Tech Stack

- **Backend**: FastAPI
- **Database**: SQLite (via SQLAlchemy)
- **Schema Validation**: Pydantic
- **Server**: Uvicorn

## Test Coverage

We used `pytest` and `coverage` to test the API, database integration, and core logic.

```bash
coverage run -m pytest
coverage report
coverage html


## How to Run the Server Locally

###  Clone & Install

```bash
git clone https://github.com/kansa05/ComplimentAPI.git
cd ComplimentAPI
python -m venv venv
.\venv\Scripts\activate   # On Windows
pip install -r requirements.txt

