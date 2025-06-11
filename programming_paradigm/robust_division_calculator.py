# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division with error handling.
    Args:
        numerator (str): The numerator input as a string.
        denominator (str): The denominator input as a string.
    Returns:
        float or str: The division result or an error message.
    """
    # Convert inputs to floats with error handling
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Handle division by zero
    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."