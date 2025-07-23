# models/professional_service.py

from extensions import db

class ProfessionalService(db.Model):
    __tablename__ = 'professional_services'

    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'),
                                primary_key=True, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'),
                           primary_key=True, nullable=False)

    # Additional fields:
    custom_fee = db.Column(db.Numeric(10, 2), nullable=True)
    notes = db.Column(db.String(200), nullable=True)

    # Inverse relationships:
    professional = db.relationship("Professional", back_populates="professional_services")
    service = db.relationship("Service", back_populates="professional_services")

    # Representation method:
    def __repr__(self):
        return f"<ProfessionalService {self.professional_id} - {self.service_id}>"
