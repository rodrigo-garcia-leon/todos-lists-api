# todo-lists

Todo Lists API using Flask.

## Requirements

- Python 3.10.0

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
curl http://127.0.0.1:5000/
python -m pytest tests/
```

## Docker

```sh
docker build -t todo-lists .
docker run -p 5000:5000 -t todo-lists 
```
