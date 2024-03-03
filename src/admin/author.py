from src.admin.base import SecureModelView


class AuthorView(SecureModelView):
    column_list = ["first_name_", "last_name_", "birth_year", "death_year", "books"]

    column_labels = {"first_name_": "სახელი", "last_name_": "გვარი", "birth_year": "დაბადების წელი",
                     "death_year": "გარდაცვალების წელი", "books": "წიგნები", "gender": "სქესი"}

    column_searchable_list = ["first_name_", "last_name_"]
