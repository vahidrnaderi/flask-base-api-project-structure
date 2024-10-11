from functools import wraps
from flask import request

from app.util import jsonify

def json_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.content_type != "application/json":
            return jsonify(
                metadata = {
                    "message": "Content type is not supported."
                },
                status=415,
            )
        else:
            return f(*args, **kwargs)

    return wrapper
