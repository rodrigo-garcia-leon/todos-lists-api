from unittest.mock import Mock
from flask import g

from app import create_app

app = create_app()
client = app.test_client()


def test_hello_world():
    response = client.get('/')

    assert b'Hello World' in response.data


def test_todos():
    with app.app_context():
        g.db = Mock()
        g.db.todos.find.return_value = [{
            "title": "test title",
            "description": "test description",
            "done": False
        }]

        response = client.get('/todos')

        assert [{
            "title": "test title",
            "description": "test description",
            "done": False
        }] == response.json
