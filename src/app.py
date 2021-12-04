from flask import Flask, request
from flask_restful import Api, Resource
from db import get_db


class Todos(Resource):
    def get(self):
        db = get_db()
        todos = list(db.todos.find({}, {'_id': False}))

        return todos, 200

    def post(self):
        todo = {
            "title": request.get_json()['title'],
            "done": False
        }

        db = get_db()
        db.todos.insert_one(dict(todo))

        return todo, 201

    def patch(self):
        todo = request.get_json()

        db = get_db()
        db.todos.update_one({"title": todo['title']}, {
                            "$set": {"done": todo['done']}})

        return todo, 200

    def delete(self):
        todo = {
            "title": request.get_json()['title'],
        }

        db = get_db()
        db.todos.delete_one(todo)

        return todo, 200


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Todos, '/todos')

    return app
