# pylint: disable=no-self-use
"""Resources"""

from flask import request
from flask_restful import Resource, marshal_with

from daos import TodosDao, CommentsDao
from models import CommentsModel, TodosModel, todos_fields, comments_fields


class TodosResource(Resource):
    """Todos Resource"""

    @marshal_with(todos_fields)
    def get(self):
        """ Get todos"""
        todos = TodosDao.read()

        return todos

    @marshal_with(todos_fields)
    def post(self):
        """Post todo"""
        todo = TodosModel(**request.get_json())
        TodosDao.create(todo)

        return todo, 201

    @marshal_with(todos_fields)
    def patch(self):
        """Patch todo"""
        todo = TodosModel(**request.get_json())
        TodosDao.update(todo)

        return todo, 200

    def delete(self):
        """Delete todo"""
        todo = TodosModel(**request.get_json())
        TodosDao.delete(todo)

        return '', 204


class CommentsResource(Resource):
    """Todos Resource"""

    @marshal_with(comments_fields)
    def get(self):
        """ Get todos"""
        comments = CommentsDao.read()

        return comments

    @marshal_with(comments_fields)
    def post(self):
        """Post todo"""
        comment = CommentsModel(**request.get_json())
        TodosDao.create(comment)

        return comment, 201
