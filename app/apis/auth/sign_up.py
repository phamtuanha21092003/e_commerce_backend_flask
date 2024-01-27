from flask import Blueprint, g
from app.utilities.validator import validate_body
from app.helpers.schemas import AccountSchema
from app.services import AccountService, session_scope

sign_up_api = Blueprint("sign_up_api", __name__)

account_service = AccountService()


@sign_up_api.route("/sign_up", methods=["POST"])
@validate_body(AccountSchema)
def sign_up():
    body = g.body
    with session_scope():
        account_service.create(**body)

    return {"status": "Sign up successfully"}
