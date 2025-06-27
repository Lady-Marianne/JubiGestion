# endpoints/person_routes.py:

from flask import Blueprint, jsonify
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

@person_bp.route("/delete_person/<kind>/<int:person_id>", methods=["PATCH"])
def delete_person(kind, person_id):
    model_class = MODEL_MAP.get(kind.lower())

    if not model_class:
        return jsonify({"error": f"Tipo de persona desconocido: {kind}"}), 400

    person = model_class.query.get_or_404(person_id)

    if person.status == PersonStatus.ELIMINADO:
        return jsonify({"message": "La persona ya está eliminada."}), 200

    try:
        person.status = PersonStatus.ELIMINADO
        db.session.commit()
        return jsonify({"message": f"{kind.capitalize()} eliminado correctamente."}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error al eliminar: {str(e)}"}), 500
