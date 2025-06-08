# # models/teacher.py

from extensions import db
from models.base_person import BasePerson

# Teacher:
class Teacher(BasePerson):
    __tablename__ = 'teachers'

    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id"), nullable=False)  # Foreign key to the activity table.

    def __repr__(self):
        return f"<Teacher {self.first_names} {self.last_name}>"