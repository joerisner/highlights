"""
Application Factory.
Reference: https://flask.palletsprojects.com/en/stable/tutorial/factory/.
"""

import contextlib
import os

from flask import Flask


def create_app(test_config=None) -> Flask:
    """
    Create and configure the application. Any configuration, registration, and other setup the application
    needs will happen inside the function. Returns the application.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "db/dev.sqlite"))

    if test_config is None:
        # load the instance config if it exists
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists (suppresses OSError)
    with contextlib.suppress(OSError):
        os.makedirs(app.instance_path)

    @app.route("/health")
    def healthcheck():
        return {"status": "UP"}, 200

    return app
