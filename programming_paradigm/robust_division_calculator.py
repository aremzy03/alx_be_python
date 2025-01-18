def safe_divide(numerator, denominator):
    numerator = int(numerator)
    denominator = int(denominator)
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by Zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return result
