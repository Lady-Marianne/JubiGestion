# models/enums.py:

from models.base_enum import BaseEnum
from sqlalchemy import Enum as SQLAlchemyEnum

class PersonStatus(BaseEnum):
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    ELIMINADO = "ELIMINADO"

class ActivityStatus(BaseEnum):
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    CANCELADO = "CANCELADO"

class AppointmentStatus(BaseEnum):
    PROGRAMADO = "PROGRAMADO"
    COMPLETADO = "COMPLETADO"
    CANCELED = "CANCELADO"

class Gender(BaseEnum):
    M = "M"
    F = "F"

    def __str__(self):
        return "Masculino" if self == Gender.M else "Femenino"
class Profession(BaseEnum):
    ABOGADO = "ABOGADO"
    ENFERMERO = "ENFERMERO"
    REFLEXÓLOGA = "REFLEXÓLOGA"
    MÉDICO_DE_CABECERA = "MÉDICO DE CABECERA"
    NUTRICIONISTA = "NUTRICIONISTA"
    PSICÓLOGO = "PSICÓLOGO"
    PSIQUIATRA = "PSIQUIATRA"
    PODÓLOGO = "PODÓLOGO"

class PaymentStatus(BaseEnum):
    PENDIENTE = "PENDIENTE"
    PAGADO = "PAGADO"
    CANCELADO = "CANCELADO"
