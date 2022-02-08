# pylint: disable=assigning-non-slot
"""Test suite for Todo Lists Flask API."""

from unittest.mock import Mock
from flask import g
from bson import ObjectId

# pylint: disable-next=import-error
from app import create_app
from models import TodosModel

app = create_app()
client = app.test_client()


def test_get_todos():
    """Test get todos."""
    with app.app_context():
        g.db = Mock()
        g.db.todos.find.return_value = [{
            "_id": ObjectId("012345678901234567890123"),
            "title": "Buy milk",
            "done": False,
            "comments": []
        }]
        response = client.get('/todos')
        g.db.todos.find.assert_called_once_with({})

        assert response.status_code == 200
        assert response.json == [{
            "_id": "012345678901234567890123",
            "title": "Buy milk",
            "done": False,
            "comments": []
        }]


def test_post_todos():
    """Test post todos."""
    with app.app_context():
        g.db = Mock()

        response = client.post('/todos', json={
            "_id": "012345678901234567890123",
            "title": "Buy milk",
        })
        g.db.todos.insert_one.assert_called_once_with({
            "_id": ObjectId("012345678901234567890123"),
            "title": "Buy milk",
            "done": False,
            "comments": []
        })

        assert response.status_code == 201
        assert response.json == {
            "_id": "012345678901234567890123",
            "title": "Buy milk",
            "done": False,
            "comments": []
        }


def test_patch_todos():
    """Test patch todos."""
    with app.app_context():
        g.db = Mock()

        response = client.patch('/todos', json={
            "_id": "012345678901234567890123",
            "title": "Buy milk",
            "done": True,
            "comments": []
        })
        g.db.todos.update_one.assert_called_once_with(
            {"_id": ObjectId('012345678901234567890123')}, {"$set": {"done": True}})

        assert response.status_code == 200
        assert response.json == {
            "_id": "012345678901234567890123",
            "title": "Buy milk",
            "done": True,
            "comments": []
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


def test_get_todo_by_id():
    """Test get todo by id."""
    with app.app_context():
        g.db = Mock()
        g.db.todos.find_one.return_value = {
            "_id": ObjectId("012345678901234567890123"),
            "title": "Buy milk",
            "done": False,
            "comments": []
        }
        response = client.get('/todo/012345678901234567890123')
        g.db.todos.find_one.assert_called_once_with(
            {'_id': ObjectId('012345678901234567890123')})

        assert response.status_code == 200
        assert response.json == {
            "_id": "012345678901234567890123",
            "title": "Buy milk",
            "done": False,
            "comments": []
        }


def test_update_todo_by_id():
    """Test put todo by id."""
    with app.app_context():
        g.db = Mock()
        g.db.todos.update_one.return_value = {
            "title": "Buy milk 2",
            "done": False,
            "comments": ["comment"]
        }
        data = {
            "title": "Buy milk 2",
            "done": False,
            "comments": ["comment"]
        }
        response = client.patch('/todo/012345678901234567890123', json=data)
        g.db.todos.update_one.assert_called_once_with(
            {'_id': ObjectId('012345678901234567890123')}, {
                "$set": data})

        assert response.status_code == 201
        assert response.json == {
            '_id': '012345678901234567890123',
            "title": "Buy milk 2",
            "done": False,
            "comments": ["comment"]
        }
