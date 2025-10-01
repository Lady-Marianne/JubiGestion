# # models/member.py:

from extensions import db
from models.base_person import BasePerson
from utils.validators import is_valid_affiliate_number
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums import MemberType, HealthPlan


# Member (Center affiliate):
class Member(BasePerson):
    
    __tablename__ = 'members'

    member_type = db.Column(SQLAlchemyEnum(MemberType), nullable=False, default=MemberType.JUBILADO)  # e.g., 'JUBILADO', 'PENSIONADO', 'ADHERENTE'.
    health_plan = db.Column(SQLAlchemyEnum(HealthPlan), nullable=False, default=HealthPlan.PAMI)  # e.g., 'PAMI', 'IAPOS', etc.
    other_health_plan = db.Column(db.String(100), nullable=True)  # If health_plan is 'OTRA', specify here.
    year = db.Column(db.Integer, nullable=True) # I don't know what this is for, keeping it nullable (Ask Ana).
    
    _affiliate_number = db.Column("affiliate_number", db.String(20), nullable=True)

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
        if value is not None:
            valid, error = is_valid_affiliate_number(value)
            if not valid:
                raise ValueError(f"Número de afiliado inválido: {error}")
        self._affiliate_number = value