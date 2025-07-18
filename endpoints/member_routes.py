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

@member_bp.route('/editar_socio/<int:member_id>', methods=['GET'])
def edit_member_form(member_id):
    member = Member.query.get_or_404(member_id)
    return render_template("member_templates/edit_member.html", member=member.to_dict())

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
            "member_id": new_member.id,
            "dni": new_member.dni
        }), 201
    
    # Handle IntegrityError for unique constraints (like DNI):
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "El nro. de DNI ya existe"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
@member_bp.route('/update_member/<int:member_id>', methods=['POST', 'PUT'])
def update_member(member_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        member = Member.query.get(member_id)
        if not member:
            return jsonify({"error": "Socio no encontrado"}), 404

        parsed_dates = parse_dates(data, ['birth_date', 'join_date'])

        new_dni = generate_full_dni(data.get('gender'), data.get('dni'))
        print("member.dni:", member.dni, type(member.dni))
        print("new_dni:", new_dni, type(new_dni))
        # Check if the new DNI is different from the current one:
        if new_dni != member.dni:
            member.dni = new_dni
        member.first_names = data.get('first_names', member.first_names)
        member.last_name = data.get('last_name', member.last_name)
        member.birth_date = parsed_dates.get('birth_date', member.birth_date)
        member.phone = data.get('phone', member.phone)
        member.email = data.get('email', member.email)
        member.address = data.get('address', member.address)
        member.status = data.get('status', member.status)
        member.join_date = parsed_dates.get('join_date', member.join_date)
        member.pami_number = data.get('pami_number', member.pami_number)

        db.session.commit()

        return jsonify({"message": "Socio actualizado exitosamente"}), 200         
        
    # Handle IntegrityError for unique constraints (like DNI):
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Ya hay otro socio con ese DNI."}), 400  
    
    # Handle other exceptions:
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
