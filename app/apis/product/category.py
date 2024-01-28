from flask import Blueprint, g
from app.utilities.jwt import required_jwt

category_api = Blueprint("category_api", __name__)


@category_api.route("/categories", methods=["GET"])
@required_jwt
def get_categories():
    return {"status": "Get categories successfully"}
