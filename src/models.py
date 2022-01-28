"""Models"""

from dataclasses import dataclass, field
from flask_restful import fields
from bson import ObjectId


todos_fields = {
    '_id': fields.String,
    'title': fields.String,
    'done': fields.Boolean,
    'comments': fields.List(fields.String)
}


@dataclass
class TodosModel:
    """Todos Model"""
    _id: ObjectId = field(default=None)
    title: str = ''
    done: bool = False
    comments: list[str] = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self._id, str):
            self._id = ObjectId(self._id)
