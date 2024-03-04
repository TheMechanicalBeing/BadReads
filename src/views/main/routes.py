from os import path

from flask import Blueprint, render_template

from src.config import Config


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "main")
main_bp = Blueprint("main_bp", __name__, template_folder=TEMPLATE_FOLDER)


@main_bp.get("/")
@main_bp.get("/home")
def home_get():
    return render_template("home_unauthorized.html", title="Home")
