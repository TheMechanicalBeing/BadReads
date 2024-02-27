from src.extensions import db
from src.models import BaseModel


class Author(db.Model, BaseModel):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    human = db.relationship("Human", uselist=False)

    def __init__(self, human_id, birth_year=None, death_year=None):
        self.birth_year = birth_year
        self.death_year = death_year
        self.human_id = human_id
