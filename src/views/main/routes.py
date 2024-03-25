from os import path

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user

from src.config import Config
from src.views.main.forms import SearchForm


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "main")
main_bp = Blueprint("main_bp", __name__, template_folder=TEMPLATE_FOLDER)


@main_bp.get("/")
@main_bp.get("/home")
def home_get():
    if current_user.is_authenticated:
        return render_template("home_authorized.html", title="Home")
    else:
        return render_template("home_unauthorized.html", title="Home")


@main_bp.route("/search/<book_name>", methods=["GET", "POST"])
def search(book_name):
    search_form = SearchForm()
    book_name = ""
    if search_form.validate_on_submit():
        book_name = search_form.search.data
        return redirect(url_for("storage_bp.storage", search_form=search_form))
    return redirect(request.referrer)
