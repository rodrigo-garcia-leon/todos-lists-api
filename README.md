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

```sh
FLASK_APP=./src/app.py flask init-db
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
