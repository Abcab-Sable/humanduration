def clamp(value: float, minimum: float, maximum: float) -> float:
    if value >= minimum and value <= maximum:
        return value
    elif value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        print("Something went wrong at clamp")