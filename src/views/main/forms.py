from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField


class SearchForm(FlaskForm):
    search = StringField("search")
    submit = SubmitField("submit")
