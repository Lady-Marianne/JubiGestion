# models/activity_enrollment.py:

from datetime import date
from extensions import db
from sqlalchemy import func
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums import ActivityStatus

# Activity Enrollment (Linking members to activities):

class ActivityEnrollment(db.Model):
    __tablename__ = 'activity_enrollments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_dni = db.Column(db.String(8), db.ForeignKey('members.dni'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False, default=func.current_date())
    status = db.Column(SQLAlchemyEnum(ActivityStatus), nullable=False, default=ActivityStatus.ACTIVE)

    member = db.relationship("Member", back_populates="activity_enrollments")
    activity = db.relationship("Activity", back_populates="activity_enrollments")

    def __repr__(self):
        return f"<ActivityEnrollment {self.id} for {self.member_dni} in {self.activity_id}>"
