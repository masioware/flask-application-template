from http import HTTPStatus

from flask import Blueprint, jsonify

hc = Blueprint("Health Check", __name__)


@hc.route("/health-check")
def heath_check():
    return jsonify(status="OK"), HTTPStatus.OK


def init(app):
    app.register_blueprint(hc)
