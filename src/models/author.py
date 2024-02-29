from src.extensions import db
from src.models import BaseModel, HumanMixin


class Author(db.Model, HumanMixin, BaseModel):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)

    books = db.relationship("Book", secondary="authors_books", back_populates="authors")

    def __init__(self, first_name, last_name, gender_id, birth_year=None, death_year=None):
        super().__init__(first_name=first_name, last_name=last_name, gender_id=gender_id)
        self.birth_year = birth_year
        self.death_year = death_year

    def __repr__(self):
        return f"<Author: {self.first_name}, {self.last_name}, {self}>"


class AuthorBook(db.Model, BaseModel):
    __tablename__ = "authors_books"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __init__(self, author_id, book_id):
        self.author_id = author_id
        self.book_id = book_id

    def __repr__(self):
        return f"<AuthorBook: {self.author_id} -> {self.book_id}>"
