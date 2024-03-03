from src.admin.base import SecureModelView


class BookView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ['_title', 'publication_year', "authors"]
