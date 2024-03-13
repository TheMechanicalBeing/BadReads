from src.extensions import db
from src.models import BaseModel


class Reading(db.Model, BaseModel):
    __tablename__ = 'readings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    book_version_id = db.Column(db.Integer, db.ForeignKey('book_versions.id'))
    page = db.Column(db.Integer, default=0)

    user = db.relationship("User", backref=db.backref("reading"))
    book = db.relationship("Book", backref=db.backref("reading"))
    book_version = db.relationship("BookVersion", backref=db.backref("reading"))

    def __init__(self, user_id, book_id, book_version_id, page=0):
        self.user_id = user_id
        self.page = page
        self.book_id = book_id
        self.book_version_id = book_version_id

    def __repr__(self):
        return f'<Reading {self.id}>'


class WantToRead(db.Model, BaseModel):
    __tablename__ = 'want_to_reads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    user = db.relationship("User", backref=db.backref("want_to_read"))
    book = db.relationship("Book", backref=db.backref("want_to_read"))

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def __repr__(self):
        return f'<Want To Read {self.id}>'


class Read(db.Model, BaseModel):
    __tablename__ = 'reads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    book_version_id = db.Column(db.Integer, db.ForeignKey('book_versions.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    user = db.relationship("User", backref=db.backref("read"))
    book = db.relationship("Book", backref=db.backref("read"))
    book_version = db.relationship("BookVersion", backref=db.backref("read"))

    def __init__(self, user_id, book_id, book_version_id, start_date, end_date):
        self.user_id = user_id
        self.book_id = book_id
        self.book_version_id = book_version_id
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f'<Read {self.id}>'
