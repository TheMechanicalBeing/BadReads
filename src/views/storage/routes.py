from os import path

from flask import Blueprint, render_template, request

from src.config import Config
from src.models import Book, Author, AuthorBook
from src.views.storage.forms import StorageFilter

TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "storage")
storage_bp = Blueprint("storage_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/storage")


@storage_bp.route("/", methods=["GET", "POST"])
@storage_bp.route("/books", methods=["GET", "POST"])
def storage_get():
    form = StorageFilter()
    books = Book.query

    if request.method == "POST":
        if form.validate_on_submit():
            if title_data := form.title.data:
                books = books.filter(Book.title.ilike(f"%{title_data}%"))

            if author_data := form.author.data:
                books = books.join(AuthorBook).join(Author).filter(Author.first_name_.ilike(f"%{author_data}%") | Author.last_name_.ilike(f"%{author_data}"))

            if publish_from_data := form.publish_from.data:
                books = books.filter(Book.publication_year >= publish_from_data)

            if publish_to_data := form.publish_to.data:
                books = books.filter(Book.publication_year <= publish_to_data)

    books = books.all()
    return render_template("storage.html", books=books, form=form)
