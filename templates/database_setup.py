from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Crear la app de Flask:
app = Flask(__name__)

# Crear la carpeta "database" si no existe:
if not os.path.exists("database"):
    os.makedirs("database")

# Configuración de la base de datos SQLite:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/jubigestion.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos:
db = SQLAlchemy(app)

# Modelo de ejemplo (puede eliminarse luego):
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Crear la base de datos y las tablas:
with app.app_context():
    db.create_all()

print("Base de datos creada correctamente.")
