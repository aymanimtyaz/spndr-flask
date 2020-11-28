from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError

class LoginForm(FlaskForm):

    email = StringField(label = 'Email', validators = [DataRequired(), Email(message = 'Please Enter a Valid Email')])
    password = PasswordField(label = 'Password', validators = [DataRequired()])
    submit_button = SubmitField(label = 'Login')

