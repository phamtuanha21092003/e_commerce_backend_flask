from flask import Blueprint, g
from app.helpers import SignInSchema, AccountSchema
from app.services import AccountService
from app.utilities.validator import validate_body
from app.helpers.errors import UBadRequest
from app.utilities.jwt import generate_token
from app.utilities.constants import ACCESS_TOKEN_LIVE_TIME, REFRESH_TOKEN_LIVE_TIME

sign_in_api = Blueprint("sign_in_api", __name__)

account_service = AccountService()


@sign_in_api.route("/sign_in", methods=["POST"])
@validate_body(SignInSchema)
def sign_in():
    body = g.body
    account = account_service.find_first(**body)
    if not account:
        raise UBadRequest("Invalid email or password")
    account = AccountSchema().dump(account)
    payload_access_token = {"id_account_id": account["id"], "role": account["role"]}
    payload_refresh_token = {
        "id_account_id": account["id"],
    }
    access_token = generate_token(payload_access_token, ACCESS_TOKEN_LIVE_TIME)
    refresh_token = generate_token(payload_refresh_token, REFRESH_TOKEN_LIVE_TIME, False)
    return {
        "status": "Sign in successfully",
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user_id": account["id"],
        "role": account["role"],
        "username": account["username"],
    }
