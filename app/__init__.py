from flask import Flask
from Instance.config import app_config
from db import create_tables
from flask_jwt_extended import JWTManager

# creating the app

jwt = JWTManager()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    app_config['JWT_SECRET_KEY'] = "this is my secret"
    jwt.init_app(app)

    ''' method to create all tables '''

    create_tables()

    from app.api.v2 import version_2 as v2
    app.register_blueprint(v2)
    return app
