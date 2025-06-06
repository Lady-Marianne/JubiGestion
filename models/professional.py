# mdodels/professional.py:

from datetime import date
from extensions import db
from sqlalchemy import func
from models.base_person import BasePerson
from utils.dni_utils import generate_full_dni

# Professional:

class Professional(BasePerson):
    __tablename__ = 'professionals'

    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(20), unique=True, nullable=True)  # Professional license number.
    profession = db.Column(db.String(100), nullable=False)  # e.g., "Psychologist", "Nutritionist".
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.
    join_date = db.Column(db.Date, nullable=False, default=func.current_date())
   
    def __repr__(self):
        return f"<Professional {self.first_names} {self.last_name}>"