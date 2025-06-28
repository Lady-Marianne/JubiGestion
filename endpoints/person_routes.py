# endpoints/person_routes.py:

from flask import Blueprint, jsonify, render_template, request
from models.member import Member
from models.professional import Professional
from models.teacher import Teacher
from models.enums import PersonStatus
from extensions import db

person_bp = Blueprint("person", __name__)

# Map types to model classes:
MODEL_MAP = {
    "member": Member,
    "professional": Professional,
    "teacher": Teacher
}

@person_bp.route("/ver_personas", methods=["GET"])
def show_persons():
    return render_template("person_templates/show_persons.html")

@person_bp.route('/all/<kind>', methods=['GET'])
def get_all_persons(kind):
    try:
        model_class = MODEL_MAP.get(kind.lower())
        if not model_class:
            return jsonify({"error": f"Tipo de persona desconocido: {kind}"}), 400
        
        # Obtain status by query param (?status=ACTIVO), default = ACTIVO
        status_str = request.args.get("status", "ACTIVO").upper()

        try:
            status_enum = PersonStatus[status_str]
        except KeyError:
            return jsonify({"error": f"Estado inválido: {status_str}"}), 400

        persons = model_class.query \
            .filter_by(status=status_enum) \
            .order_by(model_class.last_name.asc()) \
            .all()

        return jsonify([p.to_dict() for p in persons]), 200
    
    except Exception as e:
        print(f"ERROR AL TRAER {kind.upper()}S:", e)
        return jsonify({"error": str(e)}), 500

@person_bp.route("/delete_person/<kind>/<int:person_id>", methods=["PATCH"])
def delete_person(kind, person_id):
    model_class = MODEL_MAP.get(kind.lower())

    if not model_class:
        return jsonify({"error": f"Tipo de persona desconocido: {kind}"}), 400

    person = model_class.query.get_or_404(person_id)

    if person.status == PersonStatus.ELIMINADO:
        return jsonify({"message": f"El {kind.capitalize()} ya está eliminado."}), 200

    try:
        person.status = PersonStatus.ELIMINADO
        db.session.commit()
        return jsonify({"message": f"{kind.capitalize()} eliminado correctamente."}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error al eliminar: {str(e)}"}), 500
