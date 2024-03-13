from src.admin.base import SecureModelView


class ReadingView(SecureModelView):
    column_list = ["user.username", "book.title", "page", "book_version.pages"]

    column_labels = {'user.username': "მომხმარებელი", "book.title": "სათაური", "page": "წაკითხული გვერდები",
                     "book_version.pages": "გვერდები ჯამში", "user": "მომხმარებელი", "book": "წიგნი",
                     "book_version": "წიგნის გამოცემა"}


class WantToReadView(SecureModelView):
    column_list = ["user.username", "book.title"]

    column_labels = {'user.username': "მომხმარებელი", "book.title": "სათაური", "user": "მომხმარებელი", "book": "წიგნი"}


class ReadView(SecureModelView):
    column_list = ["user.username", "book.title", "start_date", "end_date"]

    column_labels = {'user.username': "მომხმარებელი", "book.title": "სათაური", "user": "მომხმარებელი", "book": "წიგნი", "start_date": "კითხვის დასაწყისი", "end_date": "კითხვის დასასრული", "book_version": "წიგნის გამოცემა"}
