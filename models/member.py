# # models/member.py:

from extensions import db
from models.base_person import BasePerson
from utils.validators import is_valid_pami_number

# Member (Center affiliate):
class Member(BasePerson):
    
    __tablename__ = 'members'

    _pami_number = db.Column("pami_number", db.String(14), nullable=True)

    activity_enrollments = db.relationship("ActivityEnrollment", back_populates="member", cascade="all, delete-orphan")
    
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