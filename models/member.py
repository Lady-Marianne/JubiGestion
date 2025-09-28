# # models/member.py:

from extensions import db
from models.base_person import BasePerson
from utils.validators import is_valid_pami_number
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums import MemberType

# Member (Center affiliate):
class Member(BasePerson):
    
    __tablename__ = 'members'

    member_type = db.Column(SQLAlchemyEnum(MemberType), nullable=False, default=MemberType.JUBILADO)  # e.g., 'JUBILADO', 'PENSIONADO', 'ADHERENTE'.
    health_plan = db.Column(db.String(50), nullable=True, default='PAMI')  # e.g., 'PAMI', 'IAPOS', etc.
    _affiliate_number = db.Column("affiliate_number", db.String(20), nullable=True)
    notes = db.Column(db.Text, nullable=True)

    activity_enrollments = db.relationship("ActivityEnrollment", 
                                           back_populates="member",
                                           cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Member {self.id} - {self.dni}>"
    
    @property
    def affiliate_number(self):
        return self._affiliate_number
    
    @affiliate_number.setter
    def affiliate_number(self, value):
        self._affiliate_number = value