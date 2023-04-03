import pytest
from . import app as application

@pytest.fixture()
def app():
    app = application
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_server_start(client):
    response = client.get("/")
    assert response.json["starting"] == "Running..."
