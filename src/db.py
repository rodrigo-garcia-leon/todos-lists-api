from os import environ
from flask import g
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/" if "MONGO_URI" not in environ else environ["MONGO_URI"]


def get_db():
    if "db" not in g:
        client = MongoClient(MONGO_URI)
        g.db = client['todo-lists']

    return g.db
