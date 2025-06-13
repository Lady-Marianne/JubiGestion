# app.py:

# Import necessary modules from Flask and database setup:

import os
from flask import Flask, render_template

# Importing extensions and database setup functions:

from extensions import db, migrate, init_app
from database_setup import create_database

# Importing the blueprint for member routes:

from endpoints.member_routes import member_bp
from endpoints.activity_routes import activity_bp

# Configure the Flask app and database:

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'jubigestion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_app(app)  # Initialize extensions (SQLAlchemy and Migrate).
create_database(app)  # Create the database if it doesn't exist.

# Define a route for the home page:

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(member_bp, url_prefix='/api/members')
app.register_blueprint(activity_bp, url_prefix='/api/activities')

if __name__ == '__main__':
    app.run(debug=True)