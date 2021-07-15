from app import app
from flask import render_template, redirect, url_for
from app.forms import CreateProjectForm, CreateTodoForm
from app.models import Project, Task
from datetime import datetime

# html 반환용
@app.route('/', method=['GET'])
def re1():
    return redirect(url_for('project'))
@app.route('/project', method=['GET'])
def project():
    form = CreateProjectForm
    
    return render_template('project.html', title='Project', form=form, projects=projects, post_url=, recent_url=)

@app.route('/project/<project_id>', method=['GET'])
def re2():
    return redirect(url_for('todo'))
@app.route('/project/<project_id>/todo', method=['GET'])
def todo():
    return render_template('todo.html', title='Todo', form=form, todos=todos)


# json 반환용   jsonify
@app.route('/api/projects', method=['GET'])
@app.route('/api/projects', method=['POST'])
def create-project:
    if form.validate_on_submit():
        db.session.add(project)
        db.session.commit()
@app.route('/api/projects/<project_id>', method=['DELETE'])
@app.route('/api/projects/<project_id>/todos', method=['GET'])
@app.route('/api/projects/<project_id>/todos', method=['POST'])
@app.route('/api/projects/<project_id>/todos/<task_id>', method=['PUT'])
@app.route('/api/projects/<project_id>/todos/<task_id>', method=['DELETE'])