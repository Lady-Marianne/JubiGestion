# mdodels/professional.py:

from extensions import db
from models.base_person import BasePerson
from models.enums import Profession
from models.enums import SqlAlchemyEnum

# Professional:
class Professional(BasePerson):
    __tablename__ = 'professionals'
  
    license_number = db.Column(db.String(20), unique=True, nullable=True)  # Professional license number.
    profession = db.Column(db.Enum(SqlAlchemyEnum(Profession)), nullable=False)

    appointments = db.relationship("Appointment", back_populates="professional", cascade="all, delete-orphan")
    