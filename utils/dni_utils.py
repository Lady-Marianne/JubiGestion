# utils/dni_utils.py:

def generate_full_dni (gender: str, dni_number: str) -> str:
    """
    Generate a valid DNI (national ID) by combining gender and the numeric string.
    :param gender: A string, either 'M' (male) or 'F' (female).
    :param dni_number: A numeric string with 7 or 8 digits.
    :return: A valid DNI string, e.g. '12345678' or 'F1234567'.
    :raises ValueError: If gender or dni_number are invalid.
    """
    gender = gender.upper()
    if gender not in ['M', 'F']:
        raise ValueError("The 'gender' field must be either 'M' or 'F'.")

    if not dni_number or not dni_number.isdigit():
        raise ValueError("The DNI number must contain only digits.")

    if len(dni_number) == 8:
        full_dni = dni_number
    elif len(dni_number) == 7:
        full_dni = f"{gender}{dni_number}"
    else:
        raise ValueError("The DNI number must have 7 or 8 digits.")

    # If model_class is provided, check for uniqueness:
    """
        existing = model_class.query.filter(model_class.dni == full_dni).first()
        if existing and (current_person_id is None or existing.id != current_person_id):
            raise ValueError("Validación manual: El nro. de DNI ya existe.")
    """
    return full_dni
