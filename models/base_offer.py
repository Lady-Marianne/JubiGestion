# models/base_offer.py:

from extensions import db
from models.base_model import BaseModel
from sqlalchemy import func, Enum as SQLAlchemyEnum
from models.enums import ActivityStatus

class BaseOffer(BaseModel):
    __abstract__ = True  # SQLAlchemy does not convert it into a table.

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    schedule = db.Column(db.String(100), nullable=True)  # e.g., "Monday, Wednesday 10:00-12:00".
    start_date = db.Column(db.Date, nullable=False, default=func.current_date())
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(SQLAlchemyEnum(ActivityStatus), nullable=False, default=ActivityStatus.ACTIVO)

    def __repr__(self):
        return f"<BaseOffer {self.name} ({str(self.status)})>"    