# # models/member.py:

from extensions import db
from models.base_person import BasePerson
from utils.validators import is_valid_pami_number

# Member (Center affiliate):
class Member(BasePerson):
    
    __tablename__ = 'members'
    health_insurance = db.Column(db.String(100), nullable=True)  # e.g., "PAMI", "IAPOS", "OSDE", etc.
    health_insurance_number = db.Column(db.String(20), nullable=False)  # e.g., "1234567890".
    # _pami_number = db.Column("pami_number", db.String(14), nullable=True)
    age = db.Column(db.Integer, nullable=False)  # Age in years.
    marital_status = db.Column(db.String(20), nullable=False)  # e.g., "Soltero", "Casado", etc.

    activity_enrollments = db.relationship("ActivityEnrollment", 
                                           back_populates="member",
                                           cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Member {self.id} - {self.dni}>"
    
    @property
    def pami_number(self):
        return self._pami_number
    
    @pami_number.setter
    def pami_number(self, value):
        is_valid, error = is_valid_pami_number(value)        
        if not is_valid:
            raise ValueError(error)
        self._pami_number = value