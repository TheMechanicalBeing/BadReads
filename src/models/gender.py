from src.extensions import db
from src.models import BaseModel


class Gender(db.Model, BaseModel):
    __tablename__ = "genders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Gender: {self.name}>"
