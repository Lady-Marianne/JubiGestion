# utils/validators.py:

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True, None
    else:
        return False, "Ingrese un correo electrónico válido."
    
def is_valid_pami_number(pami_number, current_member_id=None):
    """
    Validates the PAMI number format:
    - It can be null (if the member does not have a PAMI number).
    - If it isn't null, it must be a string of 14 digits and must be unique
    (excluding the current member, if editing).

    Args:
        pami_number (str or None): The PAMI number to validate.
    Returns:
        tuple: (is_valid (bool), error_message (str or None))
    """
    if not pami_number:
        return True, None
    if len(pami_number) != 14 or not pami_number.isdigit():
        return False, "El número de PAMI debe tener 14 dígitos."
    return True, None

