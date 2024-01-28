import os
from flask import Blueprint, g
from app.helpers.errors import UBadRequest
from app.utilities.validator import validate_body
from app.helpers.validators import RefreshSchema
from app.utilities.jwt import decode_token, generate_token
from app.services import AccountService
from app.helpers import AccountSchema
from app.utilities.constants import ACCESS_TOKEN_LIVE_TIME, REFRESH_TOKEN_LIVE_TIME

refresh_api = Blueprint("refresh_api", __name__)

account_service = AccountService()


@refresh_api.route("/refresh", methods=["POST"])
@validate_body(RefreshSchema)
def refresh():
    body = g.body
    decode_data = decode_token(
        body["token"],
        secret_key=os.getenv("JWT_SECRET_KEY_REFRESH_TOKEN"),
        algorithm=os.getenv("JWT_ALGORITHM"),
    )
    account = account_service.find_by_id(decode_data["id_account_id"], "id", "role")
    if not account:
        raise UBadRequest("Invalid token")

    account = AccountSchema().dump(account)
    payload_access_token = {"id_account_id": account["id"], "role": account["role"]}
    payload_refresh_token = {
        "id_account_id": account["id"],
    }
    access_token = generate_token(payload_access_token, ACCESS_TOKEN_LIVE_TIME)
    refresh_token = generate_token(
        payload_refresh_token, REFRESH_TOKEN_LIVE_TIME, False
    )

    return {
        "status": "Refresh successfully",
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user_id": account["id"],
    }
