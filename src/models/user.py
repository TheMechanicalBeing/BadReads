from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db
from src.models import BaseModel, HumanMixin


class User(db.Model, HumanMixin, UserMixin, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    username = db.Column(db.String)
    email_address = db.Column(db.String)
    phone_number = db.Column(db.String)
    _password = db.Column(db.String)

    role = db.relationship("Role", uselist=False)

    def __init__(self, first_name, last_name, gender_id, role_id, username, email_address, phone_number, password):
        super().__init__(first_name=first_name, last_name=last_name, gender_id=gender_id)
        self.role_id = role_id
        self.username = username
        self.email_address = email_address
        self.phone_number = phone_number
        self._password = password

    def __repr__(self):
        return f'<User: {self.username}>'

    @property
    def is_admin(self):
        return self.role_id == 2

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._password, password)
