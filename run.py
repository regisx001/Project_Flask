from datetime import timedelta
from flask import Flask, redirect, render_template, url_for
from app.config import Config
from app.models.db import db, init_db
from app.controllers.auth_controller import auth_bp
from flask_session import Session  # <-- Add this import


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="app/templates",
                static_folder='app/static', static_url_path='/static')
    app.config.from_object(config_class)

    # Configure Flask-Session
    app.config['SESSION_TYPE'] = 'sqlalchemy'  # Store sessions in database
    # Use your existing SQLAlchemy instance
    app.config['SESSION_SQLALCHEMY'] = db
    app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'  # Custom table name
    app.config['SESSION_PERMANENT'] = True  # Sessions persist
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(
        hours=1)  # 1 hour expiration

    # Initialize database
    init_db(app)

    # Initialize Flask-Session AFTER db initialization
    Session(app)  # <-- Add this line

    # Register blueprints
    app.register_blueprint(auth_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
