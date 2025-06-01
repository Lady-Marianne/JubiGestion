from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Crear la carpeta "database" si no existe:
if not os.path.exists("database"):
    os.makedirs("database")

db = SQLAlchemy()

# Base model: Member (Center affiliate):
class Member(db.Model):
    __tablename__ = 'members'

    dni = db.Column(db.String(8), unique=True, primary_key=True, nullable=False)
    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    pami_number = db.Column(db.String(14), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.
    join_date = db.Column(db.Date, nullable=False, default=date.today)

    def __repr__(self):
        return f"<Member {self.first_names} {self.last_name}>"

# Create the database (if it doesn't exist) and the tables:
def create_database(app):
    # Si querés usar la carpeta "database/", actualizá el path aquí también
    if not os.path.exists('jubigestion.db'):
        with app.app_context():
            db.create_all()
            print("Base de datos creada exitosamente.")
    else:
        print("La base de datos ya existe.")        