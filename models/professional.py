# mdodels/professional.py:

from database import db

# Professional:

class Professional(db.Model):
    __tablename__ = 'professionals'

    dni = db.Column(db.String(8), unique=True, primary_key=True, nullable=False)
    first_names = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)  # e.g., "Psychologist", "Nutritionist".
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'inactive', etc.
    
    def __repr__(self):
        return f"<Professional {self.first_names} {self.last_name}>"