# pylint: disable=invalid-name
"""Todo Lists Flask API"""

from flask import Flask
from flask_restful import Api

from db import init_app
from resources import TodoByIdResource, TodosResource


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    api = Api(app)
    init_app(app)

    api.add_resource(TodosResource, '/todos')
    api.add_resource(TodoByIdResource, '/todo/<id>')

    return app
