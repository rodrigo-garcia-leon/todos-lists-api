# todo-lists

Todo Lists API using Flask.

## Requirements

- Python 3.10.0
- MongoDB 5.0.4

## Setup

1. Create virtual environment: `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`

## Start

```sh
FLASK_APP=./src/app.py flask run
```

## Test

```sh
pytest
pytest tests/acceptance.py
```

## Docker

```sh
docker build -t todo-lists .
docker run -p 5000:5000 -t todo-lists
```

## MongoDB

```sh
mkdir -p ~/data/db
sudo mongod --dbpath ~/data/db
docker-compose up
```

```
use todo-lists

db.todos.insertOne({
    "title": "Buy milk",
    "done": false
})

db.todos.find()
```