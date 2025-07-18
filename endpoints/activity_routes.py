# endpoints/activity_routes.py:

from flask import render_template, Blueprint, request, jsonify
from models.activity import Activity
from models.enums import ActivityStatus
from extensions import db
from sqlalchemy.exc import IntegrityError
from utils.date_utils import parse_dates

activity_bp = Blueprint('activity', __name__)

@activity_bp.route("/nueva_actividad", methods=["GET", "POST"])
def add_activity():
    return render_template("activity_templates/add_activity.html")

@activity_bp.route("/ver_actividades", methods=["GET"])
def show_activities():
    return render_template("activity_templates/show_activities.html")

@activity_bp.route('/editar_actividad', methods=['PUT'])
def edit_activity():
    activity = Activity.query.get_or_404(activity_id)
    return render_template("activity_templates/edit_activity.html", activity=activity.to_dict())

@activity_bp.route('/new', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        print("JSON recibido:", data)
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
        # Obtain status by query param (?status=ACTIVO), default = ACTIVO.
        status_str = request.args.get("status", "ACTIVO").upper()

        try:
            status_enum = ActivityStatus[status_str]
        except KeyError:
            return jsonify({"error": f"Estado inválido: {status_str}"}), 400

        activities = Activity.query.order_by(Activity.name.asc()).all()

        activities = model_class.query \
            .filter_by(status=status_enum) \
            .order_by(model_class.name.asc()) \
            .all
        
        return jsonify([a.to_dict() for a in activities])
    
    except Exception as e:
        print("ERROR AL TRAER ACTIVIDADES:", e)
        return jsonify({"error": str(e)}), 500
    
@activity_bp.route('/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        activity = Activity.query.get(activity_id)
        if not activity:
            return jsonify({"error": "Actividad no encontrada"}), 404
        
        parsed_dates = parse_dates(data, ['start_date', 'end_date'])
        
        # Update activity fields:
        activity.name = data.get('name', activity.name)
        activity.description = data.get('description', activity.description)
        activity.schedule = data.get('schedule', activity.schedule)
        activity.start_date = parsed_dates.get('start_date', activity.start_date)
        activity.end_date = parsed_dates.get('end_date', activity.end_date)
        activity.capacity = data.get('capacity', activity.capacity)
        activity.status = data.get('status', activity.status)

        db.session.commit()

        return jsonify({"message": "Actividad actualizada exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400