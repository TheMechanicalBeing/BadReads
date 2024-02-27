from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import Human, Gender, Author, Category, Book, CategoryBook, AuthorBook


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
    click.echo("Populating categories...")

    category1 = Category("autobiographical")
    category2 = Category("novel")
    category3 = Category("existential")
    category4 = Category("tragedy")

    category1.create(commit=False)
    category2.create(commit=False)
    category3.create(commit=False)
    category4.create(commit=False)

    click.echo("Categories populated")
    click.echo("Populating books...")

    book1 = Book("Tender is the Night", 1934)
    book2 = Book("Steppenwolf", 1927)

    book1.create(commit=False)
    book2.create(commit=False)

    AuthorBook(author1.id, book1.id).create(commit=False)
    AuthorBook(author2.id, book2.id).create(commit=False)

    CategoryBook(category1.id, book2.id).create(commit=False)
    CategoryBook(category2.id, book2.id).create(commit=False)
    CategoryBook(category3.id, book2.id).create(commit=False)
    CategoryBook(category4.id, book1.id).create(commit=False)

    click.echo("Books populated")

    db.session.commit()

    click.echo("Database populated")
