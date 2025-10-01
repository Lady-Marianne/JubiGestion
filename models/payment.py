# models/payment.py:

from datetime import date
from extensions import db

# Payment (Financial transaction for a member):

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    payment_month = db.Column(db.String(20), nullable=False)  # e.g., 'Enero'
    payment_year = db.Column(db.Integer, nullable=False)  # e.g., 2025
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='PENDIENTE')  # 'PENDIENTE', 'PAGADO', etc.

    member = db.relationship('Member', backref='payments')

    def __repr__(self):
        return f"<Payment {self.payment_month} {self.payment_year} for Member {self.member_id}>"