from flask import Blueprint, g
from .category import category_api

product_api = Blueprint("product_api", __name__)

product_api.register_blueprint(category_api)