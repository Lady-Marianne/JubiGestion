# database_setup.py:

from extensions import db
from sqlalchemy import inspect # Importing inspect to check if the table exists.
import os

# Create directory "database" if it doesn't exist:
if not os.path.exists("database"):
    os.makedirs("database")
    print ("Carpeta 'database' creada exitosamente.")
else:
    print ("La carpeta 'database' ya existe.")

# Create the database (if it doesn't exist) but NOT the tables:
def create_database(app):
    db_path = 'database/jubigestion.db'
    print(f"Ruta de la base de datos: {db_path}")
    print(f"¿Existe la base? {os.path.exists(db_path)}")
    if not os.path.exists(db_path):
        # Only create empty database file:
        open(db_path, 'a').close()
        print("Base de datos creada exitosamente (vacía, sin tablas).")
    else:
        print("La base de datos ya existe.")
        