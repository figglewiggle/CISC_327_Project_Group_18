# test_app.py
# to run the test on the command line, first type: FLASK_ENV=testing in the terminal on vscode (navigate to CISC_327 first).
# to record the output: pytest > test_results.txt on the command line or pip install pytest-html, and then pytest --html=report.html
import pytest
from app import app as flask_app
@pytest.fixture
def app():
    flask_app.config.from_object('tests.config_test.TestConfig')
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    
