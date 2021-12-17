"""Todo Lists Flask API"""

from flask import Flask, request
from flask_restful import Api, Resource

from db import get_db, init_app
from resources import TodosResource


class Comments(Resource):
    """Comments Resource"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        # pylint: disable-next=invalid-name
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
    init_app(app)

    api.add_resource(TodosResource, '/todos')

    return app
