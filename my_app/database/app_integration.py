from flask import g

from my_app.database import actions
from my_app.paths import TEST_DB_INSTANCE_NAME


def init_db():
    db = get_db()
    actions.instantiate_db(db)


def get_db():
    if "db" not in g:
        g.db = actions.connect_db(TEST_DB_INSTANCE_NAME)
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
