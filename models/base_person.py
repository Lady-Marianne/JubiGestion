# models/base_person.py:

from extensions import db
from datetime import date
from sqlalchemy import func
from utils.dni_utils import generate_full_dni

class BasePerson(db.Model):
    __abstract__ = True  # SQLAlchemy doesn`t convert it into a table.

    dni = db.Column(db.String(8), unique=True, primary_key=True, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    _dni_number = None  # Temporal, does not store in the DB, but is used to generate the complete DNI.
    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.
    join_date = db.Column(db.Date, nullable=False, default=func.current_date())

    @property
    def dni_number(self):
        return self._dni_number

    @dni_number.setter
    def dni_number(self, value):
        """
        Receives the DNI as a string of 7 or 8 digits, and processes it with the gender
        to save the final version in self.dni.
        """
        if self.gender is None:
            raise ValueError("Se debe establecer el sexo antes de asignar el número de DNI.")
        self._dni_number = value
        self.dni = generate_full_dni(self.gender, value)
