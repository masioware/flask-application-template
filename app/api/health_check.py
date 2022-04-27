from http import HTTPStatus

from flask import Blueprint, jsonify

from app.extensions.logger import logger

hc = Blueprint("Health Check", __name__)


@hc.route("/health-check")
def heath_check():
    """Route for application health check"""
    logger.info("/health-check is requested")
    return jsonify(status="OK"), HTTPStatus.OK


def init(app):
    """Register the Blueprint with an injected Flask application"""
    logger.info("starting health-check route")
    app.register_blueprint(hc)
