from src.models import db
from src.models import BaseModel


class Publisher(db.Model, BaseModel):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    books = db.relationship('Book', secondary="book_versions", back_populates="publishers")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Publisher: {self.name}>'
