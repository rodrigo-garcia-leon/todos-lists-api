# pylint: disable=invalid-name
"""Daos"""

from db import get_db
from models import TodosModel
from bson import ObjectId


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
        db.todos.insert_one(todo.__dict__)

    @staticmethod
    def update(todo: TodosModel):
        """Update"""
        db = get_db()
        db.todos.update_one({"_id": todo._id}, {
            "$set": {"done": todo.done}})

    @staticmethod
    def delete(todo: TodosModel):
        """Delete"""
        db = get_db()
        db.todos.delete_one({"title": todo.title})

    @staticmethod
    def read_by_id(id):
        """Read by id"""
        db = get_db()
        cursor = db.todos.find_one({'_id': ObjectId(id)})

        if cursor is None:
            return None

        todo = TodosModel(**cursor)

        return todo

    @staticmethod
    def update_by_id(id, todo: TodosModel):
        """Read by id"""
        db = get_db()
        cursor = db.todos.update_one({'_id': ObjectId(id)}, {
            "$set": {
                "title": todo.title,
                "done": todo.done,
                "comments": todo.comments}})

        if cursor is None:
            return None

        updated_todo = TodosModel(**cursor)

        return updated_todo
