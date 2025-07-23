# models/service.py

from extensions import db
from sqlalchemy import Enum as SQLAlchemyEnum
from models.enums import ActivityStatus

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    is_pami_covered = db.Column(db.Boolean, default=False)
    default_fee = db.Column(db.Numeric(10, 2), nullable=True)
    status = db.Column(SQLAlchemyEnum(ActivityStatus), nullable=False, default=ActivityStatus.ACTIVO)

    # Relationship one-to-many with the junction table:
    professional_services = db.relationship("ProfessionalService", back_populates="service")

    def __repr__(self):
        return f"<Service {self.id} - {self.name}>"