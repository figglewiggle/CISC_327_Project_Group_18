# conftest.py
# to r7 first).
# to record the output: pytest > test_results.txt on the command line or pip install pytest-html, and then un the test on the command line, first type: FLASK_ENV=testing in the terminal on vscode (navigate to CISC_32pytest --html=report.html
import pytest
from flask_migrate import upgrade
from ..app import create_app
from ..config import TestingConfig
@pytest.fixture(scope='session')
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        upgrade()
        yield app

@pytest.fixture
def client(app):
    return app.test_client()
        





    
    
