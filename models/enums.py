# models/enums.py:

from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

class PersonStatus(Enum):
    ACTIVE = "ACTIVO"
    SUSPENDED = "SUSPENDIDO"
    DELETED = "ELIMINADO"

class ActivityStatus(Enum):
    ACTIVE = "ACTIVO"
    SUSPENDED = "SUSPENDIDO"
    CANCELED = "CANCELADO"

class AppointmentStatus(Enum):
    SCHEDULED = "PROGRAMADA"
    COMPLETED = "COMPLETADA"
    CANCELED = "CANCELADA"

class Gender(Enum):
    MALE = "M"
    FEMALE = "F"