from flask import Blueprint, g
from app.helpers import SignInSchema
from app.services import AccountService
from app.utilities.validator import validate_body
from app.helpers.errors import UBadRequest

sign_in_api = Blueprint("sign_in_api", __name__)

account_service = AccountService()

@sign_in_api.route("/sign_in", methods=["POST"])
@validate_body(SignInSchema)
def sign_in():
    body = g.body
    account = account_service.find_first(**body)
    if not account:
        raise UBadRequest("Invalid email or password")
    return {"status": "Sign in successfully"}