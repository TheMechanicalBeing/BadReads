from flask import Flask

from src.models import db, User, Author, Book, BookVersion, Language, Category, BookFormat, BookTag, Read, WantToRead, \
    Reading
from src.config import Config
from src.commands import init_db, populate_db, personal_command
from src.extensions import login_manager
from src.admin import admin
from src.admin.author import AuthorView
from src.admin.book import BookView
from src.admin.book_version import BookVersionView
from src.admin.user import UserView
from src.admin.language import LanguageView
from src.admin.category import CategoryView
from src.admin.book_format import BookFormatView
from src.admin.tag import TagView
from src.admin.reading_behavior import ReadingView, ReadView, WantToReadView
from src.views import main_bp, auth_bp, storage_bp, user_bp
from src.views.main.forms import SearchForm

COMMANDS = [init_db, populate_db, personal_command]
BLUEPRINTS = [main_bp, auth_bp, storage_bp, user_bp]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    @app.context_processor
    def inject_form():
        form = SearchForm()
        return dict(search_form=form)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get_or_404(user_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session, name="მომხმარებლები", endpoint="user"))
    admin.add_view(AuthorView(Author, db.session, name="ავტორები", endpoint="author"))
    admin.add_view(BookView(Book, db.session, name="წიგნები", endpoint="book"))
    admin.add_view(BookVersionView(BookVersion, db.session, name="წიგნის გამოცემები", endpoint="book_version"))
    admin.add_view(LanguageView(Language, db.session, name="ენები", endpoint="language"))
    admin.add_view(CategoryView(Category, db.session, name="კატეგორიები", endpoint="genre"))
    admin.add_view(BookFormatView(BookFormat, db.session, name="ფორმატები", endpoint="format"))
    admin.add_view(TagView(BookTag, db.session, name="თეგები", endpoint="tag"))
    admin.add_view(ReadView(Read, db.session, name="წაკითხული", endpoint="read"))
    admin.add_view(ReadingView(Reading, db.session, name="კითხულობს", endpoint="reading"))
    admin.add_view(WantToReadView(WantToRead, db.session, name="წასაკითხი", endpoint="want_to_read"))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
