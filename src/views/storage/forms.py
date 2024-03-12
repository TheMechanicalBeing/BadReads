from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, StringField


class StorageFilter(FlaskForm):
    search = StringField("Search")
    submit = SubmitField('Filter')
