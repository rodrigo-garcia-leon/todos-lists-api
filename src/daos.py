# pylint: disable=invalid-name

from db import get_db
from models import TodosModel


class TodosDao:
    """Todos Dao"""

    @staticmethod
    def read():
        """Read"""
        db = get_db()
        cursor = db.todos.find({})
        todos = [TodosModel(**todo) for todo in cursor]

        return todos

    @staticmethod
    def create(todo: TodosModel):
        """Create"""
        db = get_db()
        db.todos.insert_one(dict(todo.__dict__))

    @staticmethod
    def update(todo: TodosModel):
        """Update"""
        db = get_db()
        db.todos.update_one({"title": todo.title}, {
            "$set": {"done": todo.done}})

    @staticmethod
    def delete(todo: TodosModel):
        """Delete"""
        db = get_db()
        db.todos.delete_one({"title": todo.title})
