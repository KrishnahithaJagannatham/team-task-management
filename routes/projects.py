from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Project, Task, User

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/dashboard')
@login_required
def dashboard():
    projects = Project.query.all()
    users = User.query.all()
    # Stats for the bento grid
    stats = {
        'total_tasks': Task.query.count(),
        'completed_tasks': Task.query.filter_by(status='Done').count(),
        'team_count': User.query.count(),
        'total_projects': Project.query.count()
    }
    return render_template('dashboard.html', projects=projects, users=users, stats=stats)

@projects_bp.route('/add_project', methods=['POST'])
@login_required
def add_project():
    name = request.form.get('name')
    if name:
        new_project = Project(name=name)
        db.session.add(new_project)
        db.session.commit()
    return redirect(url_for('projects.dashboard'))