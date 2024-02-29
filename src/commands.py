from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import HumanMixin, Gender, Author, Category, Book, CategoryBook, AuthorBook, BookFormat, BookVersion, \
    Publisher, Language, Role, User


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

    author1 = Author("francis scott", "Fitzgerald", 1, 1896, 1940)
    author2 = Author("Hermann Karl", "hesse", 1, 1877, 1962)

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
    click.echo("Populating formats...")

    format1 = BookFormat("Paperback")
    format2 = BookFormat("Hardcover")
    format3 = BookFormat("Kindle Edition")
    format4 = BookFormat("ebook")

    format1.create(commit=False)
    format2.create(commit=False)
    format3.create(commit=False)
    format4.create(commit=False)

    click.echo("Formats populated")
    click.echo("Populating publishers...")

    publisher1 = Publisher("პალიტრა L გამომცემლობა")
    publisher2 = Publisher("სულაკაურის გამომცემლობა")

    publisher1.create(commit=False)
    publisher2.create(commit=False)

    click.echo("Publishers populated")
    click.echo("Populating languages...")

    language1 = Language("English")
    language2 = Language("Georgian")

    language1.create(commit=False)
    language2.create(commit=False)

    click.echo("Languages populated")
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

    BookVersion(book1.id, publisher1.id, format1.id, language2.id, 9789941293436, 2018, 442).create(commit=False)
    BookVersion(book2.id, publisher2.id, format2.id, language2.id, 9789941151774, 2021, 252).create(commit=False)

    click.echo("Books populated")
    click.echo("Populating roles...")

    role1 = Role("User")
    role2 = Role("Administrator")

    role1.create(commit=False)
    role2.create(commit=False)

    click.echo("Roles populated")
    click.echo("Populating users...")

    user1 = User("Tornike", "Tsulukidze", 1, role2.id, "TheMechanicalBeing", "tornike.tsulukidze@gmail.com",
                 "593559933", "Pass123!")
    user2 = User("khvicha", "kvaratskhelia", 1, role1.id, "Football77", "khvicha.khvaratskhelia@live.com", "577777777",
                 "Pass777!")

    user1.create(commit=False)
    user2.create(commit=False)

    click.echo("Users populated")

    db.session.commit()

    click.echo("Database populated")


@click.command("personal-command")
@with_appcontext
def personal_command():
    book = Book.query.get(1)

    # BookVersion(book.id, 1, 1, 1, 123, 2000, 200).create()

    book_version = BookVersion.query.get(1)

    lang = Language.query.get(2)

    print(book.book_versions)
    print(book_version.book)
