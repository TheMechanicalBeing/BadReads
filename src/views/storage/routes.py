from os import path

from flask import Blueprint, render_template

from src.config import Config


TEMPLATE_FOLDER = path.join(Config.TEMPLATE_FOLDER)
storage_bp = Blueprint("storage_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/storage")


@storage_bp.route("/")
def storage_get():
    return render_template
