from src.extensions import db
from src.models import BaseModel


class Tag(db.Model, BaseModel):
    __tablename__ = "tags"

    id = db.Column(db.Integer,primary_key=True)
    name_ = db.Column(db.String, unique=True, nullable=False)

    # users = db.relationship("User", secondary="books_tags", back_populates="tags")
    # books = db.relationship("Book", secondary="books_tags", back_populates="tags")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Tag: {self.name}>"

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self, value):
        if " " in value:
            value = value.replace(" ", "-")
        self.name_ = value.lower()


class BookTag(db.Model, BaseModel):
    __tablename__ = "books_tags"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    book = db.relationship("Book", backref=db.backref("book_tag"))
    user = db.relationship("User", backref=db.backref("book_tag"))
    tag = db.relationship("Tag", backref=db.backref("book_tag"))

    def __init__(self, book_id, tag_id, user_id):
        self.book_id = book_id
        self.tag_id = tag_id
        self.user_id = user_id

    def __repr__(self):
        return f"<BookTag: {self.id}"
