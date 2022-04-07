from flask import Flask

from app.api import health_check


def create_app():
    app = Flask(__name__)

    health_check.init(app)

    return app
