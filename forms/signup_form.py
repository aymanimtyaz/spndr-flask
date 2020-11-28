from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import ValidationError

class SignupForm(FlaskForm):

    email = StringField(label = 'Email', validators = [DataRequired(message = 'Please enter a valid Email'), Email(message = 'Please enter a valid Email')])
    password = PasswordField(label = 'Password', validators = [DataRequired(message = 'A password is required'), EqualTo('confirm_password', message = 'Passwords must match')])
    confirm_password = PasswordField(label = 'Confirm password', validators = [DataRequired()])
    submit_button = SubmitField('Sign Up')
