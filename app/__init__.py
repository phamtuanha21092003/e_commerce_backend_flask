from flask import Flask
from db import db
from config import Config
from flask_migrate import Migrate
from schemas import ma
from app.apis import upload_api
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(upload_api, url_prefix="/api/upload")

    return app
