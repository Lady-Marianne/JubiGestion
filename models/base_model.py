# models/base_model.py:

from extensions import db
from enum import Enum
from datetime import date, datetime

class BaseModel(db.Model):
    __abstract__ = True  # A table is not created for this class, it serves as a base for other models.

    def to_dict(self, includeRelationships=False):

        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)

            # Convert enums to their value (For example: Gender.M -> 'M')
            if isinstance(value, Enum):
                result[column.name] = value.value
            # Convert dates to string:
            elif isinstance(value, (date, datetime)):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value

        if includeRelationships:
            for rel in self.__mapper__.relationships:
                related_value = getattr(self, rel.key)
                if related_value is None:
                    result[rel.key] = None
                elif isinstance(related_value, list):
                    result[rel.key] = [item.to_dict() for item in related_value]
                else:
                    result[rel.key] = related_value.to_dict()
                    
        return result
