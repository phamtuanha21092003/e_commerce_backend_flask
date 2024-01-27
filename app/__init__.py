from flask import Flask, jsonify
from db import db
from config import Config
from flask_migrate import Migrate
from schemas import ma
from app.apis import upload_api, sign_up_api
from flask_cors import CORS
from marshmallow import ValidationError

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
    app.register_blueprint(sign_up_api, url_prefix="/api/auth")

    return app


def _config_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        response = {"error": str(e), "message": "An unexpected error has occurred."}
        return jsonify(response), 500

    @app.errorhandler(ValidationError)
    def validation_error_handler(error):
        return (
            jsonify({"error": "Bad request", "messages": error.messages}),
            400,
        )
