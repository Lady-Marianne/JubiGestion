from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def parse_dates(data: dict, fields: list[str], date_format: str = '%Y-%m-%d') -> dict:
    """
    Converts one or more string date fields in a dictionary to datetime.date objects.
    If a value is invalid or missing, None is assigned and a warning is logged.

    Parameters:
        data (dict): The input dictionary (usually form or JSON data).
        fields (list[str]): List of keys in the dictionary to convert.
        date_format (str): Expected string format of the dates (default is '%Y-%m-%d').

    Returns:
        dict: A copy of the original dictionary with converted date fields.
    """
    result = data.copy()
    for field in fields:
        value = result.get(field)
        if not value:
            result[field] = None
            continue

        try:
            result[field] = datetime.strptime(value.strip(), date_format).date()
            logger.debug(f"parse_dates: Field '{field}' converted successfully.")
        except ValueError as e:
            logger.warning(f"parse_dates: Failed to convert field '{field}' with value '{value}': {e}")
            result[field] = None

    return result
