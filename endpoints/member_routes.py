# endpoints/member_routes.py:

from flask import render_template, Blueprint, request, jsonify
from models.member import Member
from extensions import db
from utils.dni_utils import generate_full_dni
from utils.date_utils import parse_dates
from sqlalchemy.exc import IntegrityError

member_bp = Blueprint('member', __name__)

@member_bp.route("/nuevo_socio", methods=["GET", "POST"])
def add_member():
    return render_template("member_templates/add_member.html")

@member_bp.route("/ver_socios", methods=["GET"])
def show_members():
    return render_template("member_templates/show_members.html")

@member_bp.route('/create', methods=['POST'])
def create_member():
    try:
        data = request.get_json()
        print("JSON recibido:", data)

        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        # Parse birth_date y join_date:
        parsed_dates = parse_dates(data, ['birth_date', 'join_date'])

        new_member = Member(
            dni=generate_full_dni(data.get('gender'), data.get('dni')),
            gender=data.get('gender'),
            first_names=data.get('first_names'),
            last_name=data.get('last_name'),
            birth_date=parsed_dates.get('birth_date'),
            phone=data.get('phone'),
            email=data.get('email'),
            address=data.get('address'),
            status=data.get('status', 'ACTIVO'),
            join_date=parsed_dates.get('join_date')
        )

        # Setter with validation:
        new_member.pami_number = data.get('pami_number')

        db.session.add(new_member)
        db.session.commit()

        return jsonify({
            "message": "Socio creado exitosamente",
            "member": new_member.dni
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "El nro. de DNI ya existe"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
@member_bp.route('/all', methods=['GET'])
def get_all_members():
    try:
        members = Member.query.order_by(Member.last_name.asc()).all()
        members_data = jsonify([m.to_dict() for m in members])       
        return members_data, 200
    except Exception as e:
        print("ERROR AL TRAER SOCIOS:", e)
        return jsonify({"error": str(e)}), 500