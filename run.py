from flask import Flask, redirect, url_for
from models import db
from flask_login import LoginManager
from routes.auth import auth_bp
from routes.projects import projects_bp
from routes.tasks import tasks_bp

# 1. Initialize the App FIRST
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# 2. Initialize the Database
db.init_app(app)

# 3. Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(tasks_bp)

# 4. Setup Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# 5. Define the Root Route (Now that 'app' exists)
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

# 6. Run the Application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)