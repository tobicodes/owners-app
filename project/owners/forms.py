## we need flask- WTF to help us make forms
## we need validators and FlaskForm
## we need to define what our form will look like

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class NewOwnerForm(FlaskForm):
	first_name = StringField('first_name', validators =[DataRequired()])
	last_name = StringField('last_name', validators =[DataRequired()])