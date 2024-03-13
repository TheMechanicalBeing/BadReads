from os import path

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from src.config import Config
from src.views.user.forms import UpdateAccountForm


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER, "user")
user_bp = Blueprint("user_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/user")


@user_bp.get("/settings")
@login_required
def settings_get():
    form = UpdateAccountForm()
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.username.data = current_user.username
    form.email_address.data = current_user.email_address
    form.phone_number.data = current_user.phone_number
    return render_template("settings.html", form=form)


@user_bp.post("/settings")
@login_required
def settings_post():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.email_address = form.email_address.data
        current_user.phone_number = form.phone_number.data
        current_user.save()
        flash("settings updated successfully", "success")
        return redirect(url_for("auth_bp.login_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("auth_bp.register_get", form=form))


@user_bp.get("/my_books")
@login_required
def my_books_get():
    return render_template("my_books.html")
