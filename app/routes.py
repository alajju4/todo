from app import app, db
from flask import render_template, redirect, url_for, request, flash
from app.forms import CreateProjectForm, CreateTaskForm
from app.models import Project, Task
from datetime import datetime
from werkzeug.urls import url_parse

# html 반환용
@app.route('/', methods=['GET','POST'])
@app.route('/projects', methods=['GET','POST'])
def projects():
    form = CreateProjectForm(request.form)
    if form.validate_on_submit(): 
        project = Project(projectname=form.projectname.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('projects'))
    #페이지
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.timestamp.desc()).paginate(page, app.config['PROJECTS_PER_PAGE'], False)
    # next_url = url_for('projects', page=project.next_num) if project.has_next else None
    # prev_url = url_for('projects', page=project.prev_num) if project.has_next else None
    return render_template('projects.html', title='Projects', form=form, projects=projects.items)
# , next_url=next_url, prev_url=prev_url)

@app.route('/projects/<project_id>/delete')#methods delete 쓰면 methods 오류 뜸... 안쓰니까 됨
def delete_project(project_id):
    project = Project.query.get_or_404(project_id) 
    db.session.delete(project)
    db.session.commit()
    flash('삭제 되었습니다.')  #안나오는중
    return redirect(url_for('projects'))

@app.route('/projects/<project_id>/tasks', methods=['GET'])
def tasks(project_id):
    project = Project.query.get(project_id)
    tasks = Task.query.all()
    return render_template('tasks.html', title='Task', tasks=tasks.items)

@app.route('/projects/<project_id>/tasks/create', methods=['GET','POST'])
def create_task(project_id):
    project = Project.query.get(project_id)
    form = CreateTaskForm(request.form)
    if form.validate_on_submit():
        task = Task(body=form.body.data, priority=form.priority.data, category=form.category.data, status='todo')
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('create_task.html', title='create_task', form=form, tasks=tasks.items)


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

# @app.route('/projects/<projects_id>/tasks/status', methods=['PUT'])


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

