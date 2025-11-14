def clamp(value: float, minimum: float, maximum: float) -> float:
    if minimum > maximum:
        raise ValueError("Minimum parameter at clamp must be lower than the Maximum parameter at clamp")
    
    if not isinstance(value, float) or not isinstance(minimum, float) or not isinstance(maximum, float):
        raise TypeError("All parameters at clamp must be of a float type")

    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value