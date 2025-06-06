# utils/dni_utils.py:

def generate_full_dni(gender: str, dni_number: str) -> str:
    """
    Validate and construct a unique DNI by combining the gender and the number if necessary.

    :param gender: 'M' or 'F'.
    :param dni_number: numeric string of 7 or 8 digits.
    :return: final DNI (e.g., '12345678' or 'F1234567').
    :raises ValueError: if the data does not comply with the rules.
    """
    gender = gender.upper()
    if gender not in ['M', 'F']:
        raise ValueError("El campo 'gender' debe ser 'M' o 'F'.")

    if not dni_number.isdigit():
        raise ValueError("El número de DNI debe contener sólo dígitos.")

    if len(dni_number) == 8:
        return dni_number
    elif len(dni_number) == 7:
        return f"{gender}{dni_number}"
    else:
        raise ValueError("El número de DNI debe tener 7 u 8 dígitos.")