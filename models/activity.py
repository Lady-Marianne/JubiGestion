# models/activity.py:

from datetime import date
from extensions import db
from models.enums import ActivityStatus
from sqlalchemy import Enum as SQLAlchemyEnum

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
    status = db.Column(SQLAlchemyEnum(ActivityStatus), nullable=False, default=ActivityStatus.ACTIVO)
    
    teachers = db.relationship("Teacher", back_populates="activity", cascade="all, delete-orphan")
    activity_enrollments = db.relationship("ActivityEnrollment", back_populates="activity", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Activity {self.name} ({str(self.status)})>"