from app import app
from flask import render_template, redirect, url_for
from app.forms import CreateTodoForm
from app.models import Project, Task
from datetime import datetime

@app.route('/')
@app.route('/home', method=['GET'])
def home():
    project = project.projectname
    return render_template('home.html', title='home', project=project)

@app.route('/home/project/<project_id>', method=['POST'])
def project_post():
    
    return render_template('project_create', title='create-project')
@app.route('/home/project/<project_id>', method=['DELETE'])
@app.route('/home/project/<project_id>/todo', method=['GET'])
@app.route('/home/project/<project_id>/todo', method=['PUT'])
@app.route('/home/project/<project_id>/todo', method=['POST'])
@app.route('/home/project/<project_id>/todo', method=['DELETE'])