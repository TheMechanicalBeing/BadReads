from flask_admin import Admin

from src.admin.base import SecureIndexView

admin = Admin(index_view=SecureIndexView(), name="BadReads Storage", template_mode="bootstrap4")
