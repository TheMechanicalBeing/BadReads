import re

from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Email, DataRequired, ValidationError

from src.models import User


class UpdateAccountForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Change Settings")

    def validate_phone_number(self, field):
        phone_number_compiler = re.compile(r'''^\s*
                   (\+\d{1,3}(\s|-|))?     # Lets user use regional code
                   \d{3}(\s|-|)            # First 3 digits Delimeters can be - '-'; ' ' or ''
                   ((\d{2}(\s|-|)){2}      # First format where you can section numbers dividing by 2 digits
                   \d{2}|
                   \d{3}(\s|-|)\d{3})      # Second format where you can section numbers dividing by 3 digits
                   \s*                     # Last 2 digits
                   $''', re.VERBOSE, )
        if not phone_number_compiler.search(field.data):
            raise ValidationError(f"Invalid phone number.")

    def validate_email_address(self, field):
        if User.query.filter_by(email_address=field.data).first() and field.data != current_user.email_address:
            raise ValidationError(f"This email already exists. Please try another one.")
