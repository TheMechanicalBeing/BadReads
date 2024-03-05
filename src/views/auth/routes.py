from os import path

from flask import Blueprint, render_template

from src.config import Config
from src.views.auth.forms import RegisterForm


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "auth")
auth_bp = Blueprint("auth_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/auth")


@auth_bp.route("/register")
def register_get():
    form = RegisterForm()
    return render_template("register.html", form=form)
