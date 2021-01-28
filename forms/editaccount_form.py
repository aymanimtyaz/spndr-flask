from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Optional
from wtforms import ValidationError

class EditAccountForm(FlaskForm):

    email = StringField(label = 'Email', validators = [Optional(), Email(message = 'Please enter a valid Email')])
    password = PasswordField(label = 'Password', validators = [Optional(), EqualTo('confirm_password', message = 'Passwords must match')])
    confirm_password = PasswordField(label = 'Confirm password', validators = [Optional(), EqualTo('password', message = 'Passwords must match')])
    submit_button = SubmitField('Save Changes')