import sqlite3
from sqlite3 import Connection

from click import Path

from my_app.paths import DB_DIR, DB_INSTANCE_NAME


def connect_db(db_instance_name: str = DB_INSTANCE_NAME):
    db = sqlite3.connect(db_instance_name, detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    return db


def instantiate_db(db: Connection):
    run_query_from_file(db, "create_schema.sql")


def populate_db_with_test_data(db: Connection):
    run_query_from_file(db, "insert_test_data.sql")


def run_query_from_file(db, file_path: str, directory: Path = DB_DIR):
    with open(directory / file_path, mode="r", encoding="utf8") as f:
        db.executescript(f.read())


def fetch_contract(db: Connection, contract_id: int):
    return db.execute(
        """
        SELECT * FROM dm_contract WHERE id = ?
        """,
        (contract_id,),
    ).fetchone()
