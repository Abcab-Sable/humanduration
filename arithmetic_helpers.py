# Edge cases for numbers:
#   For NaN, the function should raise an error.
#   For inf, the function should raise an error if it is the minimum.
#   For -inf, the function should raise an error if it is the maximum.

def clamp(value: float, minimum: float, maximum: float) -> float:
    try:
        if minimum > maximum:
            raise ValueError("Minimum parameter at clamp must be lower than the Maximum parameter at clamp")
    except TypeError:
        raise TypeError("minimum and maximum parameters at clamp must be of a float-like type, such that they are numerically comparable")

    try:
        if value < minimum:
            return minimum
        elif value > maximum:
            return maximum
        return value
    except TypeError:
        raise TypeError("value parameter at clamp must be of a float-like type, such that it is numerically comparable to minimum and maximum")