from src.admin.base import SecureModelView


class UserView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["username", "role.role"]

    column_labels = {"role.role": "როლი", "role": "როლი", "username": "მომხმარებლის სახელი", "gender": "სქესი",
                     "email_address": "მეილის მისამართი", "phone_number": "ტელეფონის ნომერი"}

    column_searchable_list = ["username", "role.role"]

    form_columns = ["role", "gender", "username", "email_address", "phone_number"]
