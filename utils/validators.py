# utils/validators.py:

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True, None
    else:
        return False, "Ingrese un correo electrónico válido."
    
def is_valid_pami_number(pami_number, member_model=None, current_member_dni=None):
    """
    Validates the PAMI number format and uniqueness before setting it:
    - It can be null (if the member does not have a PAMI number).
    - If it isn't null, it must be a string of 14 digits and must be unique
    (excluding the current member, if editing).

    Args:
        pami_number (str or None): The PAMI number to validate.
        member_model (db.Model): The Member model, passed to avoid circular imports.
        current_member_id (int or None): ID of the current member, if editing.   
    
    Returns:
        tuple: (is_valid (bool), error_message (str or None)).
    """
    if not pami_number:
        return True, None
    if len(pami_number) != 14 or not pami_number.isdigit():
        return False, "El número de PAMI debe tener 14 dígitos."
    if member_model:
        existing = member_model.query.filter_by(pami_number=pami_number).first()
        if existing and existing.dni != current_member_dni:
            return False, "El número de PAMI ya está registrado para otro socio."
    return True, None
