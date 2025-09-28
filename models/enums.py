# models/enums.py:

from models.base_enum import BaseEnum

class PersonStatus(BaseEnum):
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    ELIMINADO = "ELIMINADO"

class ActivityStatus(BaseEnum):
    ACTIVO = "ACTIVO"
    SUSPENDIDO = "SUSPENDIDO"
    CANCELADO = "CANCELADO"

class Gender(BaseEnum):
    M = "M"
    F = "F"

    def __str__(self):
        return "Masculino" if self == Gender.M else "Femenino"
    
class MaritalStatus(BaseEnum):
    SOLTERO = "SOLTERO"
    CASADO = "CASADO"
    CONVIVIENTE = "CONVIVIENTE"
    DIVORCIADO = "DIVORCIADO"
    VIUDO = "VIUDO"

class MemberType(BaseEnum):
    JUBILADO = "JUBILADO"      
    PENSIONADO = "PENSIONADO"   
    ADHERENTE = "ADHERENTE"

class HealthPlan(BaseEnum):
    PAMI = "PAMI"
    IAPOS = "IAPOS"
    OSECAC = "OSECAC"
    OSDE = "OSDE"
    GALENO = "GALENO"
    NINGUNA = "NINGUNA"
    OTRA = "OTRA"

class PaymentStatus(BaseEnum):
    PENDIENTE = "PENDIENTE"
    PAGADO = "PAGADO"