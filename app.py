# app.py:

# Import necessary modules from Flask and database setup:

import os
from flask import Flask, render_template

# Importing extensions and database setup functions:

from extensions import db, migrate, init_app
from database_setup import create_database

# Importing the blueprint for member routes:

from endpoints.person_routes import person_bp
from endpoints.member_routes import member_bp
from endpoints.activity_routes import activity_bp

# Importing models:

from models.activity_enrollment import ActivityEnrollment
from models.activity import Activity
from models.base_enum import BaseEnum
from models.base_person import BasePerson
from models.member import Member
from models.payment import Payment
from models.professional import Professional
from models.teacher import Teacher


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

app.register_blueprint(person_bp, url_prefix='/api/persons')
app.register_blueprint(member_bp, url_prefix='/api/members')
app.register_blueprint(activity_bp, url_prefix='/api/activities')

if __name__ == '__main__':
    app.run(debug=True)