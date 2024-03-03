from sqlalchemy.ext.declarative import declared_attr

from src.extensions import db


class HumanMixin:
    def __init__(self, first_name, last_name, gender_id):
        self.first_name_ = first_name
        self.last_name_ = last_name
        self.gender_id = gender_id

    def __repr__(self):
        return f'<HumanMixin: {self.first_name_} {self.last_name_}'

    @declared_attr
    def first_name_(self):
        return db.Column(db.String)

    @declared_attr
    def last_name_(self):
        return db.Column(db.String)

    @declared_attr
    def gender_id(self):
        return db.Column(db.Integer, db.ForeignKey('genders.id'))

    @declared_attr
    def gender(self):
        return db.relationship('Gender', uselist=False)

    @property
    def first_name(self):
        return self.first_name_

    @first_name.setter
    def first_name(self, value):
        self.first_name_ = value.title()

    @property
    def last_name(self):
        return self.last_name_

    @last_name.setter
    def last_name(self, value):
        self.last_name_ = value.title()
