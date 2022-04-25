from pytest import fixture

from app import create_app


@fixture(scope="module")
def test_client():
    """Create a Client Flask configured for testing"""
    app = create_app()

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
