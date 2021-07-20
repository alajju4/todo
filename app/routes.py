from app import app, db
from flask import render_template, redirect, url_for, jsonify
from app.forms import CreateProjectForm, CreateTaskForm
from app.models import Project, Task
from datetime import datetime

# html 반환용
@app.route('/', method=['GET'])
def re1():
    return redirect(url_for('projects'))
@app.route('/projects', method=['GET'])
def project():
    form = CreateProjectForm
    
    return render_template('projects.html', title='Projects', form=form, projects=projects, post_url=, recent_url=)

@app.route('/projects/<project_id>', method=['GET'])
def re2():
    return redirect(url_for('todos'))
@app.route('/projects/<project_id>/tasks', method=['GET'])
def todo():
    return render_template('todos.html', title='Todo', form=form, todos=todos)
@app.route('/projects/<project_id>/tasks/create', method=['GET'])
def create_task():
    form = CreateTaskForm()

    return render_template('create_task.html', title='create_task', form=form)

# json 반환용   jsonify
@app.route('/api/projects', method=['GET'])
@app.route('/api/projects', method=['POST'])
def create_project():
    form = CreateProjectForm()
    if form.validate_on_submit():
        return jsonify(
            projectname=form.projectname.data
        )
@app.route('/api/projects/<project_id>', method=['DELETE'])
def delete_project():

@app.route('/api/projects/<project_id>/tasks', method=['GET'])
@app.route('/api/projects/<project_id>/tasks', method=['POST'])
@app.route('/api/projects/<project_id>/tasks/<task_id>', method=['PUT'])
@app.route('/api/projects/<project_id>/tasks/<task_id>', method=['DELETE'])