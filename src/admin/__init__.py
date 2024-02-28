from flask_admin import Admin

from src.admin.base import SecureIndexView
from flask_admin import AdminIndexView

admin = Admin(index_view=AdminIndexView(), name="BadReads Storage", template_mode="bootstrap4")
