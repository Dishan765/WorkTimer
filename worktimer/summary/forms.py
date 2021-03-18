from flask_wtf import FlaskForm
from wtforms.fields.core import DecimalField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import SubmitField

class DateForm(FlaskForm):
  date = DateField('Choose a date')
  submitDate = SubmitField('Submit')

class converterForm(FlaskForm):
  time = DecimalField('Enter a time in hours to convert to H:M:S')
  submitTime = SubmitField('Submit')