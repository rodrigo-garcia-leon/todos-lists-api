# todos-lists-api

Todo Lists API using Flask.

[![Main](https://github.com/rodrigo-garcia-leon/todos-lists-api/actions/workflows/main.yml/badge.svg)](https://github.com/rodrigo-garcia-leon/todos-lists-api/actions/workflows/main.yml)

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

## Lint

```
pylint $(git ls-files '*.py')
```

## Format

```
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

```
use todo-lists

db.todos.insertOne({
    "title": "Buy milk",
    "done": false
})

db.todos.find()
```
