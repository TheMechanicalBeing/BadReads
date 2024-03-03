from src.admin.base import SecureModelView


class BookView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ['title', 'publication_year', "authors"]

    column_labels = {"title": "სათაური", "publication_year": "გამოცემის წელი", "authors": "ავტორები"}

    form_columns = ["title", "publication_year", "authors"]
