from flask import Blueprint, g
from app.utilities.validator import validate_body
from .category import category_api


product_api = Blueprint("product_api", __name__)

product_api.register_blueprint(category_api)

@product_api.route("/products", methods=["POST"])
# @validate_body()
def create_product():
    pass