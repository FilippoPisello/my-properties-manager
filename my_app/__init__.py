import os

from flask import Flask, current_app

from my_app.blueprints_register import register_all_blueprints
from my_app.commands import init_db_command
from my_app.contract import bp
from my_app.database.app_integration import close_db


def create_app(test_config=None):
    """Create and configure the Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello!"

    init_app(app)

    register_all_blueprints(app)

    return app


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
