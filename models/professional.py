# mdodels/professional.py:

from extensions import db
from models.base_person import BasePerson
from models.enums import Profession

# Professional:
class Professional(BasePerson):
    __tablename__ = 'professionals'
  
    license_number = db.Column(db.String(20), unique=True, nullable=True)  # Professional license number.
    profession = db.Column(db.Enum((Profession)), nullable=False)

    appointments = db.relationship("Appointment", back_populates="professional", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<{self.first_names} {self.last_name}, Profesión: {str(self.profession)}>"
# Note: The `Profession` enum should be defined in the `models.enums` module.