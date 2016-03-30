from datetime import date

def calculate_age(born):
    """
    Calculates the user age
    """
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))