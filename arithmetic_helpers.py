from __future__ import annotations

import math
from typing import SupportsFloat

def clamp(value: SupportsFloat, minimum: SupportsFloat, maximum: SupportsFloat) -> float:

    """
    Return ``value`` constrained to the inclusive range [minimum, maximum].

    Parameters
    ----------
    value : SupportsFloat
        The input value to clamp.
    minimum : SupportsFloat
        The lower bound of the clamping range.
    maximum : SupportsFloat
        The upper bound of the clamping range.

    Returns
    -------
    float
        ``minimum`` if ``value < minimum``;
        ``maximum`` if ``value > maximum``;
        otherwise ``value`` converted to ``float``.

    Raises
    ------
    TypeError
        If any argument cannot be converted to ``float``.
    ValueError
        If ``minimum`` or ``maximum`` is NaN, or if ``minimum > maximum``.

    Notes
    -----
    * NaN is rejected because no meaningful ordering is possible.
    * Infinite values are clamped normally to the finite bound.
    * All inputs are converted to ``float`` for consistent behaviour.

    """
    
    # Duck-type Validation
    try:
        value = float(value)
        minimum = float(minimum)
        maximum = float(maximum)
    except (ValueError, TypeError):
        raise TypeError("Parameters at clamp must be real numbers")

    # Validate NaN
    if math.isnan(value) or math.isnan(minimum) or math.isnan(maximum):
        raise ValueError("Parameters at clamp cannot be NaN")

    # Normal validation of order
    if minimum > maximum:
        raise ValueError(
            "Minimum parameter at clamp must be lower than the Maximum parameter at clamp"
        )

    # Clamping logic
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    return value

