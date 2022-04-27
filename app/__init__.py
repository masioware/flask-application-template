from flask import Flask

from app.api import health_check
from app.extensions import logger


def create_app():
    """Flask application factory"""
    app = Flask(__name__)

    logger.init(app)

    health_check.init(app)

    return app
