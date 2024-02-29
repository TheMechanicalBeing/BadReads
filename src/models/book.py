from src.extensions import db
from src.models import BaseModel


class Book(db.Model, BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String)
    publication_year = db.Column(db.Integer)

    authors = db.relationship("Author", secondary="authors_books", back_populates="books")
    categories = db.relationship("Category", secondary="categories_books", back_populates="books")
    publishers = db.relationship("Publisher", secondary="book_versions", back_populates="books")
    languages = db.relationship("Language", secondary="book_versions", back_populates="books")
    book_formats = db.relationship("BookFormat", secondary="book_versions", back_populates="books")

    def __init__(self, title, publication_year):
        self._title = title
        self.publication_year = publication_year

    def __repr__(self):
        return f"<Book: {self.title} ({self.publication_year})>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.title()


class BookFormat(db.Model, BaseModel):
    __tablename__ = "book_formats"

    id = db.Column(db.Integer, primary_key=True)
    format_ = db.Column(db.String, unique=True)

    books = db.relationship("Book", secondary="book_versions", back_populates="book_formats")

    def __init__(self, format_):
        self.format_ = format_.title()


class BookVersion(db.Model, BaseModel):
    __tablename__ = "book_versions"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    book_format_id = db.Column(db.Integer, db.ForeignKey("book_formats.id"))
    language_id = db.Column(db.Integer, db.ForeignKey("languages.id"))
    isbn = db.Column(db.String, unique=True)
    publish_year = db.Column(db.Integer)
    pages = db.Column(db.Integer)

    book_format = db.relationship("BookFormat", uselist=False)
    language = db.relationship("Language", uselist=False)

    def __init__(self, book_id, publisher_id, book_format_id, language_id, isbn, publish_year, pages=0):
        self.book_id = book_id
        self.publisher_id = publisher_id
        self.book_format_id = book_format_id
        self.language_id = language_id
        self.isbn = isbn
        self.publish_year = publish_year
        self.pages = pages
