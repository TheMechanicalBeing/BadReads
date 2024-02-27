from src.extensions import db
from src.models import BaseModel


class Book(db.Model, BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String)
    publication_year = db.Column(db.Integer)

    authors = db.relationship("Author", secondary="authors_books", back_populates="books")
    categories = db.relationship("Category", secondary="categories_books", back_populates="books")

    def __init__(self, title, publication_year):
        self._title = title
        self.publication_year = publication_year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.title()
