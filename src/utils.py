def is_number(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False