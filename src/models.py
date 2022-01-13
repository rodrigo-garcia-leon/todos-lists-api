"""Models"""

from dataclasses import dataclass, field
from flask_restful import fields


todos_fields = {
    'id': fields.String,
    'title': fields.String,
    'done': fields.Boolean,
    'comments': fields.List
}

comment_fields = {
    'comment': fields.String
}


@dataclass
class CommentsModel():
    comment: str


@dataclass
class TodosModel:
    id: str = ''
    title: str = ''
    done: bool = False
    """ (!) : Pls review """
    comments: list[CommentsModel] = field(default_factory=list)
