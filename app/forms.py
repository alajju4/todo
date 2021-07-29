from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import Task, Project

class CreateProjectForm(FlaskForm):
    projectname = TextAreaField('write project name ->', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Create Project')

class CreateTaskForm(FlaskForm):
	task = TextAreaField('Write something', validators=[DataRequired(), Length(min=1, max=50)])
	priority = RadioField('priority', choices=[('H','High'),('M','Middle'),('L','Low')])
	category = RadioField('category', choices=[('W','Work'),('S','Study'),('H','Health')])
	submit = SubmitField('Create Task')
