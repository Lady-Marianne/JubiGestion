# models/appointments.py:

from datetime import datetime
from extensions import db

# Appointment:

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_dni = db.Column(db.String(8), db.ForeignKey('members.dni'), nullable=False)
    # Foreign key to the member table.
    professional_dni = db.Column(db.String(8), db.ForeignKey('professionals.dni'), nullable=False) 
    # Foreign key to the professional table.
    appointment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='scheduled')
    # 'scheduled', 'completed', 'canceled', etc.

    member = db.relationship("Member", back_populates="appointments")
    professional = db.relationship("Professional", back_populates="appointments")
    def __repr__(self):
        return f"<Appointment {self.id} for {self.member_dni} with {self.professional_dni} on {self.appointment_date}>"