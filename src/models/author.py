from src.extensions import db
from src.models import BaseModel


class Author(db.Model, BaseModel):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    human = db.relationship("Human", uselist=False)

    books = db.relationship("Book", secondary="authors_books", back_populates="authors")

    def __init__(self, human_id, birth_year=None, death_year=None):
        self.birth_year = birth_year
        self.death_year = death_year
        self.human_id = human_id


class AuthorBook(db.Model, BaseModel):
    __tablename__ = "authors_books"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __init__(self, author_id, book_id):
        self.author_id = author_id
        self.book_id = book_id
