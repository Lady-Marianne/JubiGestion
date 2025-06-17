# mdodels/professional.py:

from extensions import db
from models.base_person import BasePerson
from models.enums import Profession

# Professional:
class Professional(BasePerson):
    __tablename__ = 'professionals'
  
    license_number = db.Column(db.String(20), unique=True, nullable=True)  # Professional license number.
    profession = db.Column(db.Enum((Profession)), nullable=False)
    schedule = db.Column(db.String(100), nullable=True)  # Schedule in a string format (e.g., "Mon-Fri 9am-5pm").

    def __repr__(self):
        return f"<{self.first_names} {self.last_name}, Profesión: {str(self.profession)}>"