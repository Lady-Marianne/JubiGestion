# utils/validators.py:

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True, None
    else:
        return False, "Ingrese un correo electrónico válido."

def is_valid_affiliate_number(affiliate_number, member_model=None):
    """
    Validates the health plan number format before setting it:
    - It can be null or empty (if the member does not have a health plan).
    - If it isn't null, it must be a string of only digits.
    Args:
        health_plan (str or None): The health plan number to validate.
        member_model (db.Model): The Member model, passed to avoid circular imports.
    
    Returns:
        tuple: (is_valid (bool), error_message (str or None)).
    """
    if affiliate_number is None or str(affiliate_number).strip() == "":
        return True, None
    affiliate_number = str(affiliate_number).strip()
    if not affiliate_number.isdigit():
        return False, "El número de afiliado debe contener solo dígitos."
    return True, None