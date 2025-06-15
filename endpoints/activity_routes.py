# endpoints/activity_routes.py:

from flask import render_template, Blueprint, request, jsonify
from models.activity import Activity
from extensions import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from utils.date_utils import parse_dates

activity_bp = Blueprint('activity', __name__)

@activity_bp.route("/nueva_actividad", methods=["GET", "POST"])
def add_activity():
    return render_template("activity_templates/add_activity.html")

@activity_bp.route("/ver_actividades", methods=["GET"])
def show_activities():
    return render_template("activity_templates/show_activities.html")

@activity_bp.route('/new', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        # Convert date fields:
        parsed_dates = parse_dates(data, ['start_date', 'end_date'])
        
        new_activity = Activity(
            name=data.get('name'),
            description=data.get('description'),
            schedule=data.get('schedule'),
            start_date=parsed_dates.get('start_date'),
            end_date=parsed_dates.get('end_date'),
            capacity=data.get('capacity', 0),
            status=data.get('status', 'ACTIVO')
        )

        db.session.add(new_activity)
        db.session.commit()

        return jsonify({
            "message": "Actividad creada exitosamente",
            "activity_id": new_activity.id
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Error de integridad, verifique los datos"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@activity_bp.route('/all', methods=['GET'])
def get_all_activities():
    try:
        activities = Activity.query.order_by(Activity.name.asc()).all()
        activities_data = jsonify([a.to_dict() for a in activities])
        return activities_data, 200
    except Exception as e:
        print("ERROR AL TRAER ACTIVIDADES:", e)
        return jsonify({"error": str(e)}), 500