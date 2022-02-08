# todos-lists-api

Todos Lists API using Flask and PyMongo.

[![Main](https://github.com/rodrigo-garcia-leon/todos-lists-api/actions/workflows/main.yml/badge.svg)](https://github.com/rodrigo-garcia-leon/todos-lists-api/actions/workflows/main.yml)

## Requirements

- Python 3.10.2
- MongoDB 5.0.4
- Docker 20.10.11

## Setup

```sh
# create virtual environment
python -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# install editable package
pip install -e .
```

## Start

```sh
FLASK_APP=./src/todos_lists_api/app.py flask run
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
python -m pytest
python -m pytest tests/acceptance.py
```

## Docker

```sh
docker build -t todos-lists-api .
docker-compose up
```

## MongoDB

```sh
FLASK_APP=./src/todos_lists_api/app.py flask init-db
```

## Todo

- add pre-commit
- add error handling
- document using OpenAPI
- use gunicorn as production server
- add load testing
- add lists
- add authentication
- add users
- add logging
- add production monitoring
