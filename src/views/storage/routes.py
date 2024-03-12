from os import path

from flask import Blueprint, render_template, redirect, url_for, flash, request

from src.config import Config
from src.models import Book
from src.views.storage.forms import StorageFilter

TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "storage")
storage_bp = Blueprint("storage_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/storage")


@storage_bp.route("/", methods=["GET", "POST"])
@storage_bp.route("/books", methods=["GET", "POST"])
def storage_get():
    form = StorageFilter()
    books = Book.query.all()

    if request.method == "POST":
        if form.validate_on_submit():
            if search_data := form.search.data:
                books = Book.query.filter(Book.title.ilike(f"%{search_data}%")).all()

    return render_template("storage.html", books=books, form=form)
