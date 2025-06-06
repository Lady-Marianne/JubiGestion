# models/activitie.py:

from datetime import date
from extensions import db

# Activity:

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    schedule = db.Column(db.String(100), nullable=True)  # e.g., "Monday, Wednesday 10:00-12:00".
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    end_date = db.Column(db.Date, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)  # Maximum number of participants.
    teacher_id = db.Column(db.String(8), db.ForeignKey('teachers.dni'), nullable=False)  
    # Foreign key to the teacher.
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.

    def __repr__(self):
        return f"<Activity {self.name}>"