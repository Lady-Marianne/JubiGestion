# endpoints/activity_routes.py:
from flask import Blueprint, request, jsonify
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
    
@activity_bp.route('/activities', methods=['GET'])
def get_all_activities():
    try:
        activities = Activity.query.order_by(Activity.name.asc()).all()
        return jsonify([{
            "id": activity.id,
            "name": activity.name,
            "description": activity.description,
            "schedule": activity.schedule,
            "start_date": activity.start_date.isoformat(),
            "end_date": activity.end_date.isoformat() if activity.end_date else None,
            "max_participants": activity.capacity,
            "status": activity.status.name
        } for activity in activities]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500