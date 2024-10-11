import os


class Config:

    # =========  Global Configuration =========

    ENV = os.environ.get("FLASK_ENV", "production")

    DEBUG = bool(int(os.environ.get("FLASK_DEBUG", "0")))

    TESTING = DEBUG

    JSONIFY_PRETTYPRINT_REGULAR = True

    RESTFUL_JSON = {"indent": 2, "sort_keys": True}
