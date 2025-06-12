# # models/member.py:

from extensions import db
from models.base_person import BasePerson
from utils.validators import is_valid_pami_number

# Member (Center affiliate):
class Member(BasePerson):
    __tablename__ = 'members'

    _pami_number = db.Column("pami_number", db.String(14), nullable=True)

    activity_enrollments = db.relationship("ActivityEnrollment", back_populates="member", cascade="all, delete-orphan")
    
    """
    Appointments are not currently managed in this model, but can be added later.
    They are currently handled through WhatsApp:
    appointments = db.relationship("Appointment", back_populates="member", cascade="all, delete-orphan")
    """
    def __repr__(self):
        return f"<Member {self.first_names} {self.last_name} ({self.status})>"
    
    @property
    def pami_number(self):
        return self._pami_number
    
    @pami_number.setter
    def pami_number(self, value):
        """
        Validates the PAMI number format and uniqueness before setting it:
        It can be null (if the member does not have a PAMI number).
        If it isn't null, it must be a string of 14 digits and must be unique
        (excluding the current member, if editing).
        """
        current_dni = getattr(self, "dni", None)
        is_valid, error = is_valid_pami_number(
            value,
            member_model=Member,
            current_member_dni=current_dni
        )

        if not is_valid:
            raise ValueError(error)

        self._pami_number = value