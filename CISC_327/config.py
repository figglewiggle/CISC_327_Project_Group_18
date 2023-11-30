import os
class Config:
    SECRET_KEY = os.environ.get('SECRET KEY', 'the random string')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MIGRATIONS_DIR = 'C:/Users/saras/Documents/GitHub/CISC_327_Project_Group_18/CISC_327/migrations'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','sqlite:///site.db').replace("postgres://", "postgresql://")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database
    SECRET_KEY = 'test_secret_key'
    BCRYPT_LOG_ROUNDS = 4  # Lower number for faster tests
