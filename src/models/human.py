from src.extensions import db
from src.models import BaseModel


class Human(db.Model, BaseModel):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    _first_name = db.Column(db.String)
    _last_name = db.Column(db.String)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))

    gender = db.relationship('Gender', uselist=False)

    def __init__(self, first_name, last_name, gender_id):
        self._first_name = first_name
        self.last_name = last_name
        self.gender_id = gender_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value.title()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value.title()
