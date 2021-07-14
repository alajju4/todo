from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import Task

class CreateTodoForm(FlaskForm):
	todo = TextAreaField('Write something', validators=[DataRequired(), Length(min=1, max=50)])
	priority = RadioField('priority', choices=[('H','High'),('M','Middle'),('L','Low')])
	category = RadioField('category', choices=[('W','Work'),('S','Study'),('H','Health')])
	submit = SubmitField('Create')

class EditTodoform(FlaskForm):