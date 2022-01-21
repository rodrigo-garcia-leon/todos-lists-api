# pylint: disable=assigning-non-slot, unused-argument, invalid-name
"""MongoDB database connection"""

from os import environ
from pymongo import MongoClient
from flask import g
from flask.cli import with_appcontext
import click

MONGO_URI = "mongodb://localhost:27017/" if "MONGO_URI" not in environ else environ["MONGO_URI"]


def get_db():
    """Get database connection"""
    if "db" not in g:
        g.client = MongoClient(MONGO_URI)
        g.db = g.client['todos-lists']

    return g.db


def close_db(e=None):
    """Close database connection"""
    g.pop("db", None)
    client = g.pop("client", None)

    if client is not None:
        client.close()


def init_db():
    """Clear existing data and create collections with schemas."""
    db = get_db()

    if 'todos' in db.list_collection_names():
        db.command('drop', 'todos')

    db.command('create', 'todos', **{
        'validator': {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['id', 'title', 'done'],
                'properties': {
                    '_id': {
                        'bsonType': 'objectId',
                        'description': 'must be a ObjectId type and is not required'
                    },
                    'id': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'title': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'done': {
                        'bsonType': 'bool',
                        'description': 'must be a boolean and is required'
                    },
                    'comments': {
                        'bsonType': 'array',
                        'description': 'must be an array of strings if the field exists',
                        'items': {
                            'bsonType': 'string'
                        },
                        'uniqueItems': True
                    }
                }
            }
        },
        'validationLevel': 'strict',
        'validationAction': 'error'
    })


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create collections with schemas."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
