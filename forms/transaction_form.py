from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms import ValidationError

class TransactionForm(FlaskForm):

    item = StringField(label = 'What did you buy?', validators  =[DataRequired()])
    price = DecimalField(label = 'How much did you spend?', 
                         validators = [DataRequired(message = 'Please enter a numerical value for the price'), 
                                       NumberRange(min = 0, message = 'Price must be greater than 0')])
    vendor = StringField(label = 'Where did you buy it from?', validators = [DataRequired()])
    category = StringField(label = 'What category would you put this purchase in?', validators = [DataRequired()])
    submit_button = SubmitField(label = 'sPnD!')

