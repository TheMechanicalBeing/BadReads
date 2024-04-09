from os import path

from flask import Blueprint, render_template, request

from src.config import Config
from src.models import Book
from src.views.storage.forms import StorageFilter
from src.views.storage.utils import FilterUtilsStorage

TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "storage")
storage_bp = Blueprint("storage_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/storage")


@storage_bp.route("/", methods=["GET", "POST"])
@storage_bp.route("/books", methods=["GET", "POST"])
def storage():
    form = StorageFilter()
    filter_obj = FilterUtilsStorage(form)
    books = Book.query
    book_name = request.args.get("book_name", None)

    if request.method == "POST":
        books = filter_obj.filter_full(books)
    elif request.method == 'GET':
        if book_name:
            books = books.filter(Book.title.ilike(f"%{book_name}%"))

    books = books.all()

    return render_template("storage.html", books=books, form=form)


@storage_bp.get("/books/<book_id>")
def book_view_get(book_id):
    book = Book.query.get(book_id)
    book_versions = book.book_versions
    return render_template("book_view.html", book=book, book_versions=book_versions)
