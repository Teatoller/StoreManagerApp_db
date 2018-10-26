from flask import Flask
from Instance.config import app_config
from app.api.v2.db import salestable
# creating the app


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    salestable()

    # Use application to name our blueprint
    from app.api.v1 import version_1 as v1
    app.register_blueprint(v1)
    return app
    