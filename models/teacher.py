# # models/teacher.py

from extensions import db
from models.base_person import BasePerson
from models.activity import Activity  # Opcional pero recomendable.

# Teacher:
class Teacher(BasePerson):
    __tablename__ = 'teachers'

    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id", name ="fk_teacher_activity"), nullable=False)  # Foreign key to activities.
    activity = db.relationship("Activity", back_populates="teachers", foreign_keys=[activity_id])  # Specify foreign key.

    def __repr__(self):
        return f"<Teacher {self.first_names} {self.last_name} ({str(self.status)})>"
    
# Note: The `Activity` model should be defined in the `models.activity` module.
# The `BasePerson` class should contain common fields like `dni`, `first_name`, `last_name`, etc.