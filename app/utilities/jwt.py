import os
import datetime
import jwt
from functools import wraps
from flask import request, g
from app.helpers.errors import UPermissionDenied


def generate_token(payload=None, token_expired_in=None, is_access_token=True):
    payload = payload or {}
    secret_key = (
        os.getenv("JWT_SECRET_KEY_ACCESS_TOKEN")
        if is_access_token
        else os.getenv("JWT_SECRET_KEY_REFRESH_TOKEN")
    )
    algorithm = os.getenv("JWT_ALGORITHM")

    if not token_expired_in:
        token_expired_in = os.getenv("JWT_LIVE_TIME")
    token_expired_at = datetime.datetime.now() + datetime.timedelta(seconds=30)
    payload["exp"] = token_expired_at

    return jwt.encode(payload, secret_key, algorithm=algorithm)


def decode_token(encoded_token, leeway=0, secret_key=None, algorithm=None):
    try:
        data = jwt.decode(
            encoded_token, secret_key, algorithms=[algorithm], leeway=leeway
        )
        return data
    except Exception:
        raise UPermissionDenied


def required_jwt(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        secret_key = os.getenv("JWT_SECRET_KEY_ACCESS_TOKEN")
        algorithm = os.getenv("JWT_ALGORITHM")
        self = g
        encoded_token = verify_jwt_in_request()
        self.jwt_data = decode_token(
            encoded_token, secret_key=secret_key, algorithm=algorithm
        )
        return fn(*args, **kwargs)

    return wrapper


def verify_jwt_in_request(header_name="Authorization", header_type="Bearer"):
    jwt_header = request.headers.get(header_name)
    if not jwt_header:
        raise UPermissionDenied

    parts = jwt_header.split()
    if header_type:
        if parts[0] != header_type or len(parts) != 2:
            raise UPermissionDenied
        encoded_token = parts[1]
    else:
        if len(parts) != 1:
            raise UPermissionDenied
        encoded_token = parts[0]

    return encoded_token
