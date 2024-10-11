import os


class Config:

    # =========  Global Configuration =========

    ENV = os.environ.get("FLASK_ENV", "production")

    DEBUG = bool(int(os.environ.get("FLASK_DEBUG", "0")))

    TESTING = DEBUG

    JSONIFY_PRETTYPRINT_REGULAR = True

    RESTFUL_JSON = {"indent": 2, "sort_keys": True}

    # =========  Database Configuration =========

    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    )
    DATABASE_PATH = os.path.join(BASE_DIR, "db", "db.sqlite")
    DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "API_DATABASE_URI",
        DATABASE_URI
    )

    SQLALCHEMY_RECORD_MODIFICATIONS = DEBUG

    SQLALCHEMY_RECORD_QUERIES = DEBUG

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING
