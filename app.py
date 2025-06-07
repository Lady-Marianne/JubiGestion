# app.py:

# Import necessary modules from Flask and database setup:

from flask import Flask, render_template
from extensions import db, migrate, init_app
from database_setup import create_database
from models.member import Member  # Importing models to ensure it's registered with SQLAlchemy.
from models.professional import Professional
from models.teacher import Teacher
from models.activity import Activity
from models.activity_enrollment import ActivityEnrollment
from models.appointments import Appointment
from models.payment import Payment
import os

# Configure the Flask app and database:

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'jubigestion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_app(app)  # Initialize extensions (SQLAlchemy and Migrate).
create_database(app)  # Create the database if it doesn't exist.

# Define a route for the home page:

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)