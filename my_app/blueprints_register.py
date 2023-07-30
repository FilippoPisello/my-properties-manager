from flask import Flask

from my_app.contract import bp as contract_bp


def register_all_blueprints(app: Flask):
    """Register all the blueprints to the app."""
    app.register_blueprint(contract_bp)
