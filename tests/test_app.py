import pytest
from flask import g

from app import create_app

app = create_app()
client = app.test_client();

def test_hello_world():
    response = client.get('/')

    assert b'Hello World' in response.data

class MockTodos:
    def find(*args, **kwargs):
        return [{
            "title": "test title",
            "description": "test description",
            "done": False
        }]

class MockDb:
    def __init__(self):
        self.todos = MockTodos()

def test_todos():
    with app.app_context():
        g.db = MockDb()
        response = client.get('/todos')

        assert [{
            "title": "test title",
            "description": "test description",
            "done": False
        }] == response.json