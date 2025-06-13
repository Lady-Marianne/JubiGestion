# endpoints/activity_routes.py:

from flask import render_template, Blueprint, request, jsonify
from models.activity import Activity
from extensions import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError

activity_bp = Blueprint('activity', __name__)

# Convert dates from string to date objects (if they exist):

def convert_dates(data):
    start_date_str = data.get('start_date')
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date() if start_date_str else None

    end_date_str = data.get('end_date')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None

    return start_date, end_date

@activity_bp.route("/nueva_actividad", methods=["GET", "POST"])
def add_activity():
    return render_template("activity_templates/add_activity.html")

@activity_bp.route("/ver_actividades", methods=["GET"])
def show_activities():
    return render_template("activity_templates/show_activities.html")

@activity_bp.route('/activities/new', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        new_activity = Activity(
            name=data.get('name'),
            description=data.get('description'),
            schedule=data.get('schedule'),  # e.g., "Monday, Wednesday 10:00-12:00".
            start_date=convert_dates(data)[0],
            end_date=convert_dates(data)[1],
            capacity=data.get('capacity', 0),
            status=data.get('status', 'ACTIVO')  # Default status is 'ACTIVO'.
        )        

        db.session.add(new_activity)
        db.session.commit()
        return jsonify({"message": "Actividad creada exitosamente", "activity_id": new_activity.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Error de integridad, verifique los datos"}), 400
    
@activity_bp.route('/all', methods=['GET'])
def get_all_activities():
    try:
        activities = Activity.query.order_by(Activity.name.asc()).all()
        activities_data = jsonify([m.to_dict() for m in activities])

        return activities_data, 200
    except Exception as e:
        print("ERROR AL TRAER ACTIVIDADES:", e)
        return jsonify({"error": str(e)}), 500