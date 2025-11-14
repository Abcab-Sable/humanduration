def clamp(value: float, minimum: float, maximum: float) -> float:
    try:
        if minimum > maximum:
            raise ValueError("Minimum parameter at clamp must be lower than the Maximum parameter at clamp")

        if value < minimum:
            return minimum
        elif value > maximum:
            return maximum
        else:
            return value
    
    except TypeError:
        raise TypeError("All parameters at clamp must be of a float type")
    except:
        raise Exception("Something weird went wrong at clamp")