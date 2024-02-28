from src.extensions import db
from src.models import BaseModel


class Role(db.Model, BaseModel):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String, unique=True)

    def __init__(self, role):
        self.role = role
