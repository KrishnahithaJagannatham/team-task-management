from flask import Blueprint, render_template
from flask_login import login_required
from models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
@login_required
def list_users():
    all_users = User.query.all()
    return render_template('dashboard.html', users=all_users) # Reusing dashboard or dedicated view