# app.py:

# Import necessary modules from Flask and database setup:

import os
from flask import Flask, render_template

# Importing extensions and database setup functions:

from extensions import db, migrate, init_app
from database_setup import create_database

# Importing models to ensure it's registered with SQLAlchemy:

from models.member import Member  
from models.professional import Professional
from models.teacher import Teacher
from models.activity import Activity
from models.activity_enrollment import ActivityEnrollment
"""
from models.appointments import Appointment
(This import is commented out because it is not used in this file, by now.)
"""
from models.payment import Payment

# Importing the blueprint for member routes:

from endpoints.member_routes import member_bp

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

@app.route("/nuevo_socio", methods=["GET", "POST"])
def add_member():
    return render_template("add_member.html")

@app.route("/ver_socios", methods=["GET"])
def show_members():
    return render_template("show_members.html")

app.register_blueprint(member_bp, url_prefix='/api')  # Registering the member routes blueprint.

if __name__ == '__main__':
    app.run(debug=True)