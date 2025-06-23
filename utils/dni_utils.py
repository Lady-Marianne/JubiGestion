# utils/dni_utils.py:

def generate_full_dni (gender: str, dni_number: str, current_person_id: int = None) -> str:
    from models.base_person import BasePerson  # 👈 Importación diferida

    """
    Generate a valid DNI (national ID) by combining gender and the numeric string,
    and ensure the resulting DNI is unique in the base_person table,
    unless it belongs to the same person (identified by current_person_id).

    :param gender: A string, either 'M' (male) or 'F' (female).
    :param dni_number: A numeric string with 7 or 8 digits.
    :param current_person_id: Optional. The ID of the current person being edited.
    :return: A valid DNI string, e.g. '12345678' or 'F1234567'.
    :raises ValueError: If gender or dni_number are invalid, or if the DNI already exists
    for another person.
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

    # Uniqueness check across all people (BasePerson):
    existing = BasePerson.query.filter(BasePerson.dni == full_dni).first()
    if existing and (current_person_id is None or existing.id != current_person_id):
        raise ValueError("El nro. de DNI ya existe.")

    return full_dni
