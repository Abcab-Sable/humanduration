import math

# Edge cases for numbers:
#   For NaN, the function should raise an error.
#   For inf, the function should raise an error if it is the minimum.
#       if maximum is inf, that just means the upper bound is unbounded.
#   For -inf, the function should raise an error if it is the maximum.
#       if minimum is -inf, that just means the lower bound is unbounded.
#   If value is inf, maximum should be returned.
#   If value is -inf, minimum should be returned.


def clamp(value: float, minimum: float, maximum: float) -> float:

    # Validate NaN
    if any(math.sinan(x) for x in (value, minimum, maximum)):
        raise ValueError("Parameters at clamp cannot be NaN")

    # Handle bounds involving infinities
    # Minimum is +inf
    if math.isinf(minimum) and minimum > 0:
        if minimum > maximum:
            raise ValueError(
                "minimum parameter cannot be higher than the maximum parameter at clamp"
            )
        return minimum

    # Maximum is -inf
    if math.isinf(maximum) and maximum < 0:
        if maximum < minimum:
            raise ValueError(
                "maximum parameter cannot be lower than the minimum parameter at clamp"
            )
        return maximum

    # Normal validation of order
    if minimum > maximum:
        raise ValueError(
            "Minimum parameter at clamp must be lower than the Maximum parameter at clamp"
        )
    
    # Handle infinite value
    if math.isinf(value):
        if value > 0:
            return maximum
        else:
            return minimum

    # Clamping logic
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    return value
