from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, IntegerField


class StorageFilter(FlaskForm):
    title = StringField("Title")
    author = StringField("Author")
    publish_from = IntegerField("Publish From")
    publish_to = IntegerField("Publish To")
    submit = SubmitField('Filter')
