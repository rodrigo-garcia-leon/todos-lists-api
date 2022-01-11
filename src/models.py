"""Models"""

from dataclasses import dataclass, field
from typing import Dict, List
from typing_extensions import TypedDict
from flask_restful import fields


todos_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'done': fields.Boolean,
    'comments': fields.List
}

comments_fields = {
    'comment': fields.String
}


@dataclass
class CommentsModel(TypedDict):
    """Comments Model"""
    comment: str


@dataclass
class TodosModel:
    """Todos Model"""
    todo_id: int = 0
    title: str = ''
    done: bool = False
    comments: Dict[str, List[CommentsModel]] = field(default_factory=list)
