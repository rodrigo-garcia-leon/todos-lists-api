"""Models"""

from dataclasses import dataclass, field
from flask_restful import fields
from bson import ObjectId


todos_fields = {
    '_id': fields.String,
    'title': fields.String,
    'done': fields.Boolean,
    'comments': fields.List
}

comment_fields = {
    'comment': fields.String
}


@dataclass
class CommentsModel:
    comment: str


@dataclass
class TodosModel:
    _id: ObjectId = ''
    title: str = ''
    done: bool = False
    """ (!) : Pls review """
    comments: list[CommentsModel] = field(default_factory=list)
