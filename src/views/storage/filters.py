from src.models import Book, Author, AuthorBook


class FilterUtilsStorage:
    def __init__(self, form_obj):
        self.form_obj = form_obj

    def filter_title(self, books_query):
        if title := self.form_obj.title.data:
            return books_query.filter(Book.title.ilike(f"%{title}%"))
        else:
            return books_query

    def filter_author(self, books_query):
        if author_data := self.form_obj.author.data:
            temp_author = Author \
                            .query \
                            .filter((Author.first_name_ + " " + Author.last_name_).ilike(f"%{author_data}%")) \
                            .all()
            temp_author_ids = [author.id for author in temp_author]
            return books_query.join(AuthorBook).join(Author).filter(Author.id.in_(temp_author_ids))
        else:
            return books_query

    def filter_publish_from(self, books_query):
        if publish_from_data := self.form_obj.publish_from.data:
            return books_query.filter(Book.publication_year >= publish_from_data)
        else:
            return books_query

    def filter_publish_to(self, books_query):
        if publish_to_data := self.form_obj.publish_to.data:
            return books_query.filter(Book.publication_year <= publish_to_data)
        else:
            return books_query
