# pylint: disable=assigning-non-slot
"""Test suite for Todo Lists Flask API"""

from unittest.mock import Mock
from flask import g

from todos_lists_api.app import create_app

app = create_app()
client = app.test_client()


def test_get_todos():
    """Test get todos."""
    with app.app_context():
        g.db = Mock()
        g.db.todos.find.return_value = [{
            "title": "Buy milk",
            "done": False
        }]

        response = client.get('/todos')
        g.db.todos.find.assert_called_once_with({}, {
            "_id": False
        })

        assert response.status_code == 200
        assert response.json == [{
            "title": "Buy milk",
            "done": False
        }]


def test_post_todos():
    """Test post todos."""
    with app.app_context():
        g.db = Mock()

        response = client.post('/todos', json={
            "title": "Buy milk",
        })
        g.db.todos.insert_one.assert_called_once_with({
            "title": "Buy milk",
            "done": False
        })

        assert response.status_code == 201
        assert response.json == {
            "title": "Buy milk",
            "done": False
        }


def test_patch_todos():
    """Test patch todos."""
    with app.app_context():
        g.db = Mock()

        response = client.patch('/todos', json={
            "title": "Buy milk",
            "done": True
        })
        g.db.todos.update_one.assert_called_once_with(
            {"title": 'Buy milk'}, {"$set": {"done": True}})

        assert response.status_code == 200
        assert response.json == {
            "title": "Buy milk",
            "done": True
        }


def test_delete_todos():
    """Test delete todos."""
    with app.app_context():
        g.db = Mock()

        response = client.delete('/todos', json={
            "title": "Buy milk",
        })
        g.db.todos.delete_one.assert_called_once_with({
            "title": "Buy milk"})

        assert response.status_code == 204
        assert response.data == b''
#
