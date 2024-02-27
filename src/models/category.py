from src.extensions import db
from src.models import BaseModel


class Category(db.Model, BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String, unique=True)

    books = db.relationship('Book', secondary="categories_books", back_populates="categories")

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.lower()


class CategoryBook(db.Model, BaseModel):
    __tablename__ = 'categories_books'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __init__(self, category_id, book_id):
        self.category_id = category_id
        self.book_id = book_id
