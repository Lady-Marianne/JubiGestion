# utils/validators.py:

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True, None
    else:
        return False, "Ingrese un correo electrónico válido."
    
def is_valid_pami_number(pami_number, member_model=None):
    """
    Validates the PAMI number format before setting it:
    - It can be null or empty (if the member does not have a PAMI number).
    - If it isn't null, it must be a string of exactly 14 digits.
    Args:
        pami_number (str or None): The PAMI number to validate.
        member_model (db.Model): The Member model, passed to avoid circular imports.
    
    Returns:
        tuple: (is_valid (bool), error_message (str or None)).
    """
    if pami_number is None or str(pami_number).strip() == "":
        return True, None
    pami_number = str(pami_number).strip()
    if len(pami_number) != 14 or not pami_number.isdigit():
        return False, "El número de PAMI debe tener exactamente 14 dígitos."