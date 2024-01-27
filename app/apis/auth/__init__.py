from flask import Blueprint
from .sign_up import sign_up_api
from .sign_in import sign_in_api

auth_api = Blueprint("auth_api", __name__)

auth_api.register_blueprint(sign_up_api)
auth_api.register_blueprint(sign_in_api)