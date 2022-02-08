"""Models"""

from dataclasses import dataclass
from flask_restful import fields


todos_fields = {
    'title': fields.String,
    'done': fields.Boolean,
}


@dataclass
class TodosModel:
    """Todos Model"""
    title: str = ''
    done: bool = False
