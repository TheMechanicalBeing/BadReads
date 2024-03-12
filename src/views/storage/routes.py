from os import path

from flask import Blueprint, render_template

from src.config import Config
from src.models import Book


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "storage")
storage_bp = Blueprint("storage_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/storage")


@storage_bp.route("/")
@storage_bp.route("/books")
def storage_get():
    books = Book.query.all()
    return render_template("storage.html", books=books)
