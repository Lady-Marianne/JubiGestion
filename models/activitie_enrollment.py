# models/activitie_enrollment.py:

from datetime import date
from extensions import db

# Activity Enrollment (Linking members to activities):

class ActivityEnrollment(db.Model):
    __tablename__ = 'activity_enrollments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_dni = db.Column(db.String(8), db.ForeignKey('members.dni'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False, default=date.today)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.

    def __repr__(self):
        return f"<ActivityEnrollment {self.id} for {self.member_dni} in {self.activity_id}>"
