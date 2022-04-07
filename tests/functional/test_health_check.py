from http import HTTPStatus
from json import loads as jsonify


def test_health_check(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/health-check' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get("/health-check")

    assert response.status_code == HTTPStatus.OK
    assert jsonify(response.data) == {"status": "OK"}
