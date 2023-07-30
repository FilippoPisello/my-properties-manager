import click

from my_app.database.app_integration import init_db


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    if input("This will erase the database. Press 5 to continue: ") == "5":
        init_db()
        click.echo("Initialized the database.")
    else:
        click.echo("Database initialization aborted.")
