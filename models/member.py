# # models/member.py

from datetime import date
from extensions import db
# -*- coding: utf-8 -*-

# Member (Center affiliate):
class Member(db.Model):
    __tablename__ = 'members'

    dni = db.Column(db.String(8), unique=True, primary_key=True, nullable=False)
    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    pami_number = db.Column(db.String(14), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.
    join_date = db.Column(db.Date, nullable=False, default=date.today)

    def __repr__(self):
        return f"<Member {self.first_names} {self.last_name}>"