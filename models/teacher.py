# # models/teacher.py

from extensions import db
from models.base_person import BasePerson

# Teacher:
class Teacher(BasePerson):
    __tablename__ = 'teachers'

    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id"), nullable=False)  # Foreign key to the activity table.
    activity = db.relationship("Activity", back_populates="teacher")
