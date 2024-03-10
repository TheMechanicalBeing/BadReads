from os import path

from flask import Blueprint, render_template
from flask_login import current_user

from src.config import Config


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "main")
main_bp = Blueprint("main_bp", __name__, template_folder=TEMPLATE_FOLDER)


@main_bp.get("/")
@main_bp.get("/home")
def home_get():
    if current_user.is_authenticated:
        return render_template("home_authorized.html", title="Home")
    else:
        return render_template("home_unauthorized.html", title="home")
