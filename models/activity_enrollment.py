# models/activity_enrollment.py:

from extensions import db
from sqlalchemy import func

# Activity Enrollment (Linking members to activities):

class ActivityEnrollment(db.Model):
    __tablename__ = 'activity_enrollments'

    member_id = db.Column(db.Integer, db.ForeignKey('members.id'),
                          primary_key=True, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'),
                            primary_key=True, nullable=False)
    
    enrollment_date = db.Column(db.Date, nullable=False, default=func.current_date())

    member = db.relationship("Member", back_populates="activity_enrollments")
    activity = db.relationship("Activity", back_populates="activity_enrollments")

    def __repr__(self):
        return f"<ActivityEnrollment {self.id} for {self.member_id} in {self.activity_id}>"
