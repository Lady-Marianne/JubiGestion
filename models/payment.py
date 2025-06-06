# models/payment.py:

from datetime import date
from extensions import db

# Payment (Financial transaction for a member):

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_id = db.Column(db.String(8), db.ForeignKey('members.dni'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    period = db.Column(db.Date, nullable=False) # The period of time the payment covers.
    payment_date = db.Column(db.Date, nullable=False, default=date.today)
    status = db.Column(db.String(20), nullable=False, default='pending')  # 'pending', 'completed', etc.

    def __repr__(self):
        return f"<Payment {self.id} for Member {self.member_id}>"