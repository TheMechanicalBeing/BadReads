from src.extensions import db
from src.models import BaseModel


class Human(db.Model, BaseModel):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    _first_name = db.Column(db.String)
    _last_name = db.Column(db.String)
    birth_year = db.Column(db.DateTime)
    gender = db.Column(db.String)

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
