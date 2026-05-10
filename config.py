import os


class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
    TESTING = os.getenv("FLASK_TESTING", "0") == "1"
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
