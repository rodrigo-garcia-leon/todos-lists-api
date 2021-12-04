from flask import Flask, jsonify
from flask_restful import Api, Resource
from db import get_db


class Todos(Resource):
    def get(self):
        db = get_db()
        todos = list(db.todos.find({}, {'_id': False}))

        return jsonify(todos)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Todos, '/todos')

    return app
