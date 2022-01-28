"""Models"""

from dataclasses import dataclass, field
from flask_restful import fields


todos_fields = {
    'title': fields.String,
    'done': fields.Boolean,
    'comments': fields.List(fields.String)
}


@dataclass
class TodosModel:
    title: str = ''
    done: bool = False
    comments: list[str] = field(default_factory=list)
