def division(a, b):
    try:
        # suppose that number2 is a float
        return a / b
    except ZeroDivisionError:
        return None
