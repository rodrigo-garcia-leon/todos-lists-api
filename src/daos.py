# pylint: disable=invalid-name
"""Daos"""

from db import get_db
from models import TodosModel


class TodosDao:
    """Todos Dao"""

    @staticmethod
    def read():
        """Read"""
        db = get_db()
        cursor = db.todos.find({}, {'_id': False})
        todos = [TodosModel(**todo) for todo in cursor]

        return todos

    @staticmethod
    def create(todo):
        """Create"""
        db = get_db()
        db.todos.insert_one(dict(todo.__dict__))

    @staticmethod
    def update(todo):
        """Update"""
        db = get_db()
        db.todos.update_one({"title": todo.title}, {
            "$set": {"done": todo.done}})

    @staticmethod
    def delete(todo):
        """Delete"""
        db = get_db()
        db.todos.delete_one({"title": todo.title})
