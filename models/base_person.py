# models/base_person.py:

from extensions import db
from datetime import date
from sqlalchemy import func, Enum as SQLAlchemyEnum
from utils.dni_utils import generate_full_dni
from models.enums import PersonStatus, Gender
class BasePerson(db.Model):
    __abstract__ = True  # SQLAlchemy doesn`t convert it into a table.

    dni = db.Column(db.String(8), unique=True, primary_key=True, nullable=False)
    gender = db.Column(SQLAlchemyEnum(Gender), nullable=False)  # 'M' for Male, 'F' for Female.
    _dni_number = None  # Temporal, does not store in the DB, but is used to generate the complete DNI.
    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(SQLAlchemyEnum(PersonStatus), nullable=False, default=PersonStatus.ACTIVO)
    join_date = db.Column(db.Date, nullable=False, default=func.current_date())

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.first_names} {self.last_name}>"

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