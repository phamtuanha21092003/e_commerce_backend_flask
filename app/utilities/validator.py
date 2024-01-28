from functools import wraps
from flask import request, g


def validate_body(validate_schema, many=False):
    def is_form(content_type):
        return (
            ('application/x-www-form-urlencoded' in content_type)
            or ('multipart/form-data' in content_type)
        )

    def validate_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            content_type = request.headers.get('Content-Type', '')

            if is_form(content_type):
                data = validate_schema().load(request.form)
            else:
                json_data = request.get_json(force=True)
                data = validate_schema(many=many).load(json_data)
            g.body = data 

            return func(*args, **kwargs)

        return wrapper

    return validate_decorator