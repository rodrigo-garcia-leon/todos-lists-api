"""Auth"""

from functools import wraps
from flask import request
from flask_restful import abort
import re
import jwt

SIGNING_KEY = "AllYourBase"


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            match = re.match(r'Bearer (.*)', request.headers['Authorization'])

            if (match):
                ss = match.group(1)

                try:
                    token = jwt.decode(ss, SIGNING_KEY,
                                       algorithms=["HS256"])
                except BaseException as error:
                    print(error)

        if not token:
            abort(401, message='Token is missing')

        return func(*args, **kwargs)

    return wrapper
