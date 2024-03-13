from flask_admin.model.template import LinkRowAction

from src.admin.base import SecureModelView


class BookViewAction(LinkRowAction):
    def __init__(self, icon_class, url=None):
        super().__init__(icon_class, url)

    def render(self, context, row_id, row):
        m = self._resolve_symbol(context, 'row_actions.link')

        url = f"/storage/books/{row_id}"

        return m(self, url)


class BookView(SecureModelView):
    column_list = ['id', 'title', 'publication_year', "authors"]

    column_labels = {"title": "სათაური", "publication_year": "გამოცემის წელი", "authors": "ავტორები"}

    column_extra_row_actions = [BookViewAction("fa fa-eye")]

    form_columns = ["title", "publication_year", "authors"]
