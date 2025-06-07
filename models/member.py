# # models/member.py:

from datetime import date
from extensions import db
from sqlalchemy import func
from models.base_person import BasePerson
from utils.dni_utils import generate_full_dni

# Member (Center affiliate):
class Member(BasePerson):
    __tablename__ = 'members'

    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    pami_number = db.Column(db.String(14), unique=True, nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.
    join_date = db.Column(db.Date, nullable=False, default=func.current_date())

    activity_enrollments = db.relationship("ActivityEnrollment", back_populates="member", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Member {self.first_names} {self.last_name}>"