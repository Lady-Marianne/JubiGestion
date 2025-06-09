# # models/member.py:

from extensions import db
from models.base_person import BasePerson

# Member (Center affiliate):
class Member(BasePerson):
    __tablename__ = 'members'

    pami_number = db.Column(db.String(14), unique=True, nullable=True)
    activity_enrollments = db.relationship("ActivityEnrollment", back_populates="member", cascade="all, delete-orphan")
    appointments = db.relationship("Appointment", back_populates="member", cascade="all, delete-orphan")
    