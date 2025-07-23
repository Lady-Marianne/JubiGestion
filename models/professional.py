# mdodels/professional.py:

from extensions import db
from models.base_person import BasePerson

# Professional:
class Professional(BasePerson):
    __tablename__ = 'professionals'
  
    license_number = db.Column(db.String(20), nullable=True) # Professional license number.
    schedule = db.Column(db.String(100), nullable=True) # Schedule in a string format.

    professional_services = db.relationship("ProfessionalService",
                                            back_populates="professional",
                                            cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Professional {self.id} - {self.dni}>"