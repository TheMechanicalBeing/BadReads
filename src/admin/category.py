from src.admin.base import SecureModelView


class CategoryView(SecureModelView):
    column_labels = {"name_": "კატეგორია"}

    form_columns = ["name_"]
