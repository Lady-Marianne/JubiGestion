# models/enums.py:

from models.base_enum import BaseEnum
from sqlalchemy import Enum as SQLAlchemyEnum

class PersonStatus(BaseEnum):
    ACTIVE = "ACTIVO"
    SUSPENDED = "SUSPENDIDO"
    DELETED = "ELIMINADO"

class ActivityStatus(BaseEnum):
    ACTIVE = "ACTIVO"
    SUSPENDED = "SUSPENDIDO"
    CANCELED = "CANCELADO"

class AppointmentStatus(BaseEnum):
    SCHEDULED = "PROGRAMADO"
    COMPLETED = "COMPLETADO"
    CANCELED = "CANCELADO"

class Gender(BaseEnum):
    MALE = "M"
    FEMALE = "F"

    def __str__(self):
        return "Masculino" if self == Gender.MALE else "Femenino"
class Profession(BaseEnum):
    LAWYER = "ABOGADO"
    NURSE = "ENFERMERO"    
    MASSEUR = "MASAJISTA"
    GENERAL_PRACTITIONER = "MÉDICO DE CABECERA"
    NUTRITIONIST = "NUTRICIONISTA"
    PSYCHOLOGIST = "PSICÓLOGO"
    PSYCHIATRIST = "PSIQUIATRA"
    PODOLOGIST = "PODÓLOGO"

class PaymentStatus(BaseEnum):
    PENDING = "PENDIENTE"
    PAID = "PAGADO"
    CANCELED = "CANCELADO"
