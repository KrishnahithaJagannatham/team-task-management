from flask import Blueprint, request, redirect, url_for
from flask_login import login_required
from models import Task, db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    project_id = request.form.get('project_id')
    user_id = request.form.get('user_id')
    priority = request.form.get('priority')
    due_date = request.form.get('due_date')
    
    if title and project_id and user_id:
        new_task = Task(
            title=title, 
            project_id=project_id, 
            user_id=user_id,
            priority=priority,
            due_date=due_date
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('projects.dashboard'))

@tasks_bp.route('/update_status/<int:task_id>', methods=['POST'])
@login_required
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get('status')
    if new_status:
        task.status = new_status
        db.session.commit()
    return redirect(url_for('projects.dashboard'))