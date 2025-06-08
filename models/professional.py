# mdodels/professional.py:

from extensions import db
from models.base_person import BasePerson

# Professional:
class Professional(BasePerson):
    __tablename__ = 'professionals'
  
    license_number = db.Column(db.String(20), unique=True, nullable=True)  # Professional license number.
    profession = db.Column(db.String(100), nullable=False)  # e.g., "Psychologist", "Nutritionist".
    
    appointments = db.relationship("Appointment", back_populates="professional", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Professional {self.first_names} {self.last_name}>"