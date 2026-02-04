from flask import Flask

from app.extensions import api, db
from app.config import Config
from app.routes import register_blueprints

from . import models


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)
    db.init_app(flask_app)
    api.init_app(flask_app)

    register_blueprints(api)

    with flask_app.app_context():
        db.create_all() 

    return flask_app
