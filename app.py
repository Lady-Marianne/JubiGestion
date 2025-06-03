# app.py

# Import necessary modules from Flask and database setup:

from flask import Flask, render_template
from extensions import db
from database_setup import create_database
from models.member import Member  # Importing Member model to ensure it's registered with SQLAlchemy.
import os

# Configure the Flask app and database:
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'jubigestion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    create_database(app)

# Define a route for the home page:
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)