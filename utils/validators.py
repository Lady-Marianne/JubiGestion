# utils/validators.py:

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True, None
    else:
        return False, "Ingrese un correo electrónico válido."
