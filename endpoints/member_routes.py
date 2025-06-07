# endpoints/member_routes.py:

from flask import Blueprint, request, jsonify
from models.member import Member
from extensions import db
from utils.dni_utils import generate_full_dni
from datetime import datetime
from sqlalchemy.exc import IntegrityError

member_bp = Blueprint('member', __name__)

# Convertir fechas desde string a objetos date (si existen):
def convert_dates(data):
    birth_date_str = data.get('birth_date')
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date() if birth_date_str else None

    join_date_str = data.get('join_date')
    join_date = datetime.strptime(join_date_str, '%Y-%m-%d').date() if join_date_str else None

    return birth_date, join_date

@member_bp.route('/members', methods=['POST'])
def create_member():
    try:
        data = request.json
        print("JSON recibido:", data)
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
        new_member = Member(
            dni=generate_full_dni(data.get('gender'), data.get('dni')),
            gender=data.get('gender'),
            first_names=data.get('first_names'),
            last_name=data.get('last_name'),
            pami_number=data.get('pami_number'),
            birth_date=convert_dates(data)[0],
            phone=data.get('phone'),
            email=data.get('email'),
            address=data.get('address'),
            status=data.get('status', 'active'),
            join_date=convert_dates(data)[1]
        )
        db.session.add(new_member)
        db.session.commit()
        return jsonify({"message": "Socio creado exitosamente", "member": new_member.dni}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "El nro. de DNI o de PAMI ya existe"}), 400
    
@member_bp.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = Member.query.all()
        members_data = [
            {
                "dni": m.dni,
                "gender": m.gender,
                "first_names": m.first_names,
                "last_name": m.last_name,
                "pami_number": m.pami_number,
                "birth_date": m.birth_date.isoformat() if m.birth_date else None,
                "phone": m.phone,
                "email": m.email,
                "address": m.address,
                "status": m.status,
                "join_date": m.join_date.isoformat() if m.join_date else None
            }
            for m in members
        ]
        return jsonify(members_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
