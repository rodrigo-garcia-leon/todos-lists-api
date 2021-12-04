from flask import Flask, jsonify
from db import get_db


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello World"

    @app.route("/todos")
    def todos():
        db = get_db()
        todos = list(db.todos.find({}, {'_id': False}))

        return jsonify(todos)

    return app
