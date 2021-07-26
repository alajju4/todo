from app import app, db
from flask import render_template, redirect, url_for, request
from app.forms import CreateProjectForm, CreateTaskForm
from app.models import Project, Task
from datetime import datetime
from werkzeug.urls import url_parse

# html 반환용
@app.route('/', methods=['GET','POST'])
@app.route('/projects', methods=['GET','POST'])
def project():
    form = CreateProjectForm
    if form.validate_on_submit:
        project = Project(projectname=form.projectname.data, timestamp=datetime.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('project'))
    #페이지
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.timestamp.desc()).paginate(page, app.config['PROJECTS_PER_PAGE'], False)
    next_url = url_for('project', page=project.next_num) if project.has_next else None
    prev_url = url_for('project', page=project.prev_num) if project.has_next else None
    return render_template('projects.html', title='Projects', form=form, projects=projects.items, next_url=next_url, prev_url=prev_url)
# @app.route('/projects/<project_id>/delete', methods=['DELETE'])
# def delete_project:
#     Project.query.filter_by(project_id).delete()
#     db.session.commit()
#     return redirect(url_for('project'))

@app.route('/projects/<project_id>/', methods=['GET'])
def re2():
    return redirect(url_for('task'))
@app.route('/projects/<project_id>/tasks', methods=['GET'])
def task():
    return render_template('tasks.html', title='Task', tasks=task.items)
@app.route('/projects/<project_id>/tasks/create', methods=['GET','POST'])
def create_task():
    form = CreateTaskForm()
    if form.validate_on_submit():
        task = Task(body=form.body.data, priority=form.priority.data, category=form.category.data, status='todo')
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task'))
    return render_template('create_task.html', title='create_task', form=form, task=task.items)
# @app.route('/projects/<project_id>/tasks/edit', methods=['PUT'])
# def edit_task():
#     form = CreateTaskForm()
#     if form.validate_on_submit():
#         task = Task(body=form.body.data, priority=form.priority.data, category=form.category.data, status='todo')
#         db.session.edit(task)
#         db.session.commit()
# @app.route('/projects/<project_id>/tasks/delete', methods=['DELETE'])
# def delete_task:
#     Task.query.filter_by(Task.id).delete()
#     db.session.commit()
#     return redirect(url_for('task'))






# # json 반환용   jsonify
# @app.route('/api/projects', method=['GET'])
# @app.route('/api/projects', method=['POST'])
# def create_project():
#     return jsonify(
#         projectname = form.projectname.data,
#         timestamp = datetime.date()
#         )
# @app.route('/api/projects/<project_id>', method=['DELETE'])
# def delete_project():

# @app.route('/api/projects/<project_id>/tasks', method=['GET'])
# @app.route('/api/projects/<project_id>/tasks', method=['POST'])
#     form = CreateTaskForm()
#     if form.validate_on_submit():
#         return jsonify(
#             task=form.projectname.data
#         )
# @app.route('/api/projects/<project_id>/tasks/<task_id>', method=['PUT'])
# @app.route('/api/projects/<project_id>/tasks/<task_id>', method=['DELETE'])

if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(debug=True)