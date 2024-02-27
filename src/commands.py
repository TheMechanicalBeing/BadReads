from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import Human, Gender, Author


@click.command("init-db")
@with_appcontext
def init_db():
    click.echo("Creating database...")
    db.drop_all()
    db.create_all()
    click.echo("Database created")


@click.command("populate-db")
@with_appcontext
def populate_db():
    click.echo("Populating database...")

    click.echo("Populating genders...")

    for gender in ("male", "female", "unknown"):
        Gender(gender).create(commit=False)

    click.echo("Genders populated")
    click.echo("Populating authors...")

    human_author1 = Human("Francis Scott", "Fitzgerald",1)
    human_author2 = Human("Hermann Karl", "Hesse", 1)

    human_author1.create(commit=False)
    human_author2.create(commit=False)

    author1 = Author(human_author1.id, 1896, 1940)
    author2 = Author(human_author2.id, 1877, 1962)

    author1.create(commit=False)
    author2.create(commit=False)

    click.echo("Authors populated")

    db.session.commit()

    click.echo("Database populated")
