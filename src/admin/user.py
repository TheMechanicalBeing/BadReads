from src.admin.base import SecureModelView


class UserView(SecureModelView):
    column_list = ["username", "role.role"]

    column_labels = {"role.role": "როლი", "role": "როლი", "username": "მომხმარებლის სახელი", "gender": "სქესი",
                     "email_address": "მეილის მისამართი", "phone_number": "ტელეფონის ნომერი", "first_name_": "სახელი",
                     "last_name_": "გვარი"}

    column_searchable_list = ["username", "role.role"]

    form_columns = ["first_name_", "last_name_", "role", "gender", "username", "email_address", "phone_number"]
