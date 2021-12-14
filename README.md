# todos-lists-api

Todos Lists API using Flask and PyMongo.

[![Main](https://github.com/rodrigo-garcia-leon/todos-lists-api/actions/workflows/main.yml/badge.svg)](https://github.com/rodrigo-garcia-leon/todos-lists-api/actions/workflows/main.yml)

## Requirements

- Python 3.10.0
- MongoDB 5.0.4
- Docker 20.10.11

## Setup

```sh
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Start

```sh
FLASK_APP=./src/app.py flask run
```

## Lint

```sh
pylint $(git ls-files '*.py')
```

## Format

```sh
autopep8 --in-place $(git ls-files '*.py')
```

## Test

```sh
pytest
pytest test/acceptance.py
```

## Docker

```sh
docker build -t todos-lists-api .
docker-compose up
```

## MongoDB

```js
use todo-lists

db.todos.insertOne({
    "title": "Buy milk",
    "done": false
})

db.todos.find()
```

## Todo

- use gunicorn as production server
- add error handling
- add authentication
- add users
- add lists
- document using OpenAPI
- add load testing
- add production monitoring
- add logging
