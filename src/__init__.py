from flask import Flask
from flask_login import login_user

from src.models import db, User, Author, Book
from src.config import Config
from src.commands import init_db, populate_db, personal_command
from src.extensions import login_manager
from src.admin import admin
from src.admin.author import AuthorView
from src.admin.book import BookView
from src.admin.user import UserView


COMMANDS = [init_db, populate_db, personal_command]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)

    @app.route("/")
    def initial():
        login_user(User.query.get_or_404(1))
        return f"Hello world! {User.query.get(1).is_admin}"

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


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
