from src.admin.base import SecureModelView


class LanguageView(SecureModelView):
    column_labels = {"language": "ენა"}

    form_columns = ["language"]
