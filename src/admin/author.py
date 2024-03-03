from src.admin.base import SecureModelView


class AuthorView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["_first_name", "_last_name", "birth_year", "death_year", "books"]

    column_labels = {"_first_name": "სახელი", "_last_name": "გვარი", "birth_year": "დაბადების წელი",
                     "death_year": "გარდაცვალების წელი", "books": "წიგნები", "gender": "სქესი"}

    column_searchable_list = ["_first_name", "_last_name"]
