# pylint: disable=invalid-name
"""Todo Lists Flask API"""

from flask import Flask, request
from flask_restful import Api, Resource
from db import get_db


class Todos(Resource):
    """Todos Resource"""

    def __init__(self):
        """Constructor"""
        super().__init__()

        self.db = get_db()

    def get(self):
        """ Get todos"""
        todos = list(self.db.todos.find({}, {'_id': False}))

        return todos, 200

    def post(self):
        """Post todo"""
        todo = {
            "title": request.get_json()['title'],
            "done": False
        }

        self.db.todos.insert_one(dict(todo))

        return todo, 201

    def patch(self):
        """Patch todo"""
        todo = request.get_json()

        self.db.todos.update_one({"title": todo['title']}, {
            "$set": {"done": todo['done']}})

        return todo, 200

    def delete(self):
        """Delete todo"""
        todo = {
            "title": request.get_json()['title'],
        }

        self.db.todos.delete_one(todo)

        return todo, 200


class Comments(Resource):
    """Comments Resource"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.db = get_db()

    def get(self):
        """ Get comments"""
        comments = list(self.db.comments.find({}, {'_id': False}))
        return comments, 200

    def post(self):
        """ Post comment"""
        comment = {
            'comment': request.get_json()['comment']
        }
        self.db.comments.insert_one(dict(comment))
        return comment, 200

    def patch(self):
        """ Patch comment"""
        comment = request.get_json()
        self.db.comments.update_one({"comment": comment["comment"]},
                                    {"$set": {comment["comment"]}})
        return comment, 200

    def delete(self):
        """ Delete comment"""
        comment = {
            "comment": request.get_json()['comment']
        }
        self.db.comment.delete_one(comment)
        return comment, 200


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Todos, '/todos')

    return app
