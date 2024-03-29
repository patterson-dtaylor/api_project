import pytest
from main import app as flask_api

@pytest.fixture
def app():
    yield flask_api

@pytest.fixture
def client(app):
    return app.test_client()