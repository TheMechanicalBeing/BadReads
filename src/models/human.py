from sqlalchemy.ext.declarative import declared_attr

from src.extensions import db


class HumanMixin:
    def __init__(self, first_name, last_name, gender_id):
        self._first_name = first_name
        self.last_name = last_name
        self.gender_id = gender_id

    def __repr__(self):
        return f'<HumanMixin: {self.first_name} {self.last_name}'

    @declared_attr
    def _first_name(self):
        return db.Column(db.String)

    @declared_attr
    def _last_name(self):
        return db.Column(db.String)

    @declared_attr
    def gender_id(self):
        return db.Column(db.Integer, db.ForeignKey('genders.id'))

    @declared_attr
    def gender(self):
        return db.relationship('Gender', uselist=False)

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
