# config_test.py
class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database
    SECRET_KEY = 'test_secret_key'
    BCRYPT_LOG_ROUNDS = 4  # Lower number for faster tests