from src.extensions import db
from src.models import BaseModel


class Language(db.Model, BaseModel):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String, unique=True, nullable=False)

    books = db.relationship('Book', secondary="book_versions", back_populates="languages")

    def __init__(self, language):
        self.language = language

    def __repr__(self):
        return f"<Language: {self.language}>"
