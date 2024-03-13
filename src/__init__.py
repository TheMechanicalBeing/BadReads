from flask import Flask
from flask_login import logout_user

from src.models import db, User, Author, Book, BookVersion, Language, Category, BookFormat
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
from src.views import main_bp, auth_bp, storage_bp, user_bp


COMMANDS = [init_db, populate_db, personal_command]
BLUEPRINTS = [main_bp, auth_bp, storage_bp, user_bp]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

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


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
