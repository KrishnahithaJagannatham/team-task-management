import os

# Get the absolute path of the directory where config.py is located
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-dev-key'
    
    # Check if we are on Railway (which uses DATABASE_URL)
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Locally, create the database file in the main project folder to avoid 'instance' issues
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False