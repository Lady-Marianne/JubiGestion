# endpoints/member_routes.py:

from flask import Blueprint, request, jsonify
from models.member import Member
from extensions import db
from utils.dni_utils import generate_full_dni
from datetime import datetime
from sqlalchemy.exc import IntegrityError

member_bp = Blueprint('member', __name__)

# Convert dates from string to date objects (if they exist):

def convert_dates(data):
    birth_date_str = data.get('birth_date')
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date() if birth_date_str else None

    join_date_str = data.get('join_date')
    join_date = datetime.strptime(join_date_str, '%Y-%m-%d').date() if join_date_str else None

    return birth_date, join_date

@member_bp.route('/members', methods=['POST'])
def create_member():
    try:
        data = request.get_json()
        print("JSON recibido:", data)
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
        
        new_member = Member(
            dni=generate_full_dni(data.get('gender'), data.get('dni')),
            gender=data.get('gender'),
            first_names=data.get('first_names'),
            last_name=data.get('last_name'),
            birth_date=convert_dates(data)[0],
            phone=data.get('phone'),
            email=data.get('email'),
            address=data.get('address'),
            status=data.get('status', 'ACTIVO'),  # Default status is 'ACTIVO'.
            join_date=convert_dates(data)[1]
        )
        
        # This calls the setter for pami_number, which validates it:
        new_member.pami_number = data.get('pami_number')

        db.session.add(new_member)
        db.session.commit()
        return jsonify({"message": "Socio creado exitosamente", "member": new_member.dni}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "El nro. de DNI ya existe"}), 400
    
@member_bp.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = Member.query.order_by(Member.last_name.asc()).all()
        members_data = jsonify([m.to_dict() for m in members])       
        return members_data, 200
    except Exception as e:
        print("ERROR AL TRAER SOCIOS:", e)
        return jsonify({"error": str(e)}), 500