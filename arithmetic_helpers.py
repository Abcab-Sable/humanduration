import math

# Edge cases for numbers:
#   For NaN, the function should raise an error.
#   For inf, the function should raise an error if it is the minimum.
#       if maximum is inf, that just means the upper bound is unbounded.
#   For -inf, the function should raise an error if it is the maximum.
#       if minimum is -inf, that just means the lower bound is unbounded.

def clamp(value: float, minimum: float, maximum: float) -> float:
    try:
        if math.isnan(minimum) or math.isnan(maximum):
            raise ValueError("minimum and maximum parameters at clamp cannot be a NaN")

        if math.isinf(minimum):
            raise ValueError("minimum parameter at clamp cannot be positive-infinity")

        if math.isinf(-maximum):
            raise ValueError("maximum parameter at clamp cannot be negative-infinity")

        if minimum > maximum:
            raise ValueError("Minimum parameter at clamp must be lower than the Maximum parameter at clamp")

    except TypeError:
        raise TypeError("minimum and maximum parameters at clamp must be of a float-like type, such that they are numerically comparable")

    try:
        if math.isnan(value):
            raise ValueError("value parameter at clamp cannot be a NaN")

        if math.isinf(value):
            return maximum
        
        if math.isinf(-value):
            return minimum

        if value < minimum:
            return minimum
        elif value > maximum:
            return maximum
        return value

    except TypeError:
        raise TypeError("value parameter at clamp must be of a float-like type, such that it is numerically comparable to minimum and maximum")