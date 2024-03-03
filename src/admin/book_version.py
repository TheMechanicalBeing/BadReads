from src.admin.base import SecureModelView


class BookVersionView(SecureModelView):
    column_list = ["book_id", "isbn", "book.title", "publisher.name", "publish_year", "pages", "language.language",
                   "book_format.format_"]

    column_labels = {"book_id": "წიგნის ID", "isbn": "ISBN", "book.title": "სათაური", "publisher.name": "გამომცემელი",
                     "publish_year": "გამოცემის წელი", "pages": "გვერდების რაოდენობა", "language.language": "ენა",
                     "book_format.format_": "წიგნის ფორმატი"}
