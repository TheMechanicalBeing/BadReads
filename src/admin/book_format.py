from src.admin.base import SecureModelView


class BookFormatView(SecureModelView):
    column_labels = {"format_": "ფორმატი"}

    form_columns = ["format_"]
