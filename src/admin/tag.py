from src.admin.base import SecureModelView


class TagView(SecureModelView):
    column_list = ["id", "tag.name_","book.title", "user.username"]

    column_labels = {"tag.name": "თეგი", "book.title": "სათაური", "user.username": "მომხმარებელი", "book": "წიგნი", "User": "მომხმარებელი", "tag": "თეგი"}