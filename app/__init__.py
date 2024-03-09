from flask import Flask, jsonify
from db import db
from config import Config
from flask_migrate import Migrate
from schemas import ma
from app.apis import upload_api, auth_api, product_api
from flask_cors import CORS
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app.helpers.errors import UBadRequest, UForbidden, UPermissionDenied


migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    _config_error_handlers(app)

    app.register_blueprint(upload_api, url_prefix="/api")
    app.register_blueprint(auth_api, url_prefix="/api/auth")
    app.register_blueprint(product_api, url_prefix="/api/product")

    return app


def _config_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_error(error):
        response = {"error": str(error), "message": "An unexpected error has occurred."}
        return jsonify(response), 500

    @app.errorhandler(ValidationError)
    def validation_error_handler(error):
        return (
            jsonify({"error": "Bad request", "messages": error.messages}),
            400,
        )

    @app.errorhandler(IntegrityError)
    def integrity_error_handler(error):
        return (
            jsonify(
                {"error": "Bad request", "messages": error.orig.diag.message_detail}
            ),
            400,
        )

    @app.errorhandler(UBadRequest)
    def u_bad_request_handler(error):
        return jsonify({"error": str(error)}), 400

    @app.errorhandler(500)
    def server_error_page(error):
        return jsonify({"error": "Internal server error"}), 500

    @app.errorhandler(UForbidden)
    def forbidden(error):
        return jsonify({"error": str(error) or "Forbidden"}), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(UPermissionDenied)
    def permission_denied(error):
        return jsonify({'error': 'Permission denied'}), 401

