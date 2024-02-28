from wtforms.validators import DataRequired

from src.admin.base import SecureModelView


class UserView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["role.role", "username", "email_address", "phone_number"]

    column_labels = {"role.role": "როლი", "username": "მომხმარებლის სახელი", "email_address": "მეილის მისამართი",
                     "phone_number": "ტელეფონის ნომერი"}

    column_searchable_list = ["role.role", "username", "email_address", "phone_number"]