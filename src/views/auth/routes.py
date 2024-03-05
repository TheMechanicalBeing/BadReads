from os import path

from flask import Blueprint, render_template, flash, redirect, url_for

from src.config import Config
from src.views.auth.forms import RegisterForm
from src.models import User

TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "auth")
auth_bp = Blueprint("auth_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/auth")


@auth_bp.get("/register")
def register_get():
    form = RegisterForm()
    return render_template("register.html", form=form)


@auth_bp.post("/register")
def register_post():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO: Should add gender in forms
        # TODO: Should automate format for phone number
        user_to_register = User(form.first_name.data, form.last_name.data, 1, 1, form.username.data,
                                form.email_address.data, form.phone_number.data, form.password.data)

        user_to_register.create()
        flash("Account registered successfully", "success")
        return redirect(url_for("main_bp.home_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("auth_bp.register_get", form=form))
