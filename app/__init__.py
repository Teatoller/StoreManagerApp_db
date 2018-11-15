from flask import Flask
from Instance.config import app_config
from db import create_tables
from flask_jwt_extended import (JWTManager, jwt_required, get_raw_jwt)
# from app.api.v2.views.users import blacklist


blacklist = set()
# creating the app

# jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    app.config['JWT_SECRET_KEY'] = "this is my secret"
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKENS_CHECKS'] = ['access', 'refresh']
    jwt = JWTManager(app)
    # jwt.init_app(app)

    @jwt.token_in_blacklist_loader(callable)
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    ''' method to create all tables '''

    create_tables()

    from app.api.v2 import version_2 as v2
    app.register_blueprint(v2)
    return app
