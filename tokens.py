from .units import UNITS as u
from .exceptions import DurationParseError

test = "-1hr-2.1m-3s"

def flush_unit_token(unit_token, valid_units, duration_token, duration_tokens):
    joined_unit = "".join(unit_token)
    if joined_unit in valid_units:
        duration_token.append(joined_unit)
        duration_tokens.append(duration_token)
    else:
        raise DurationParseError(f"Invalid unit: {joined_unit}")
    return [], [], duration_tokens

def scan(dur_str):

    duration_tokens = []
    duration_token = []
    digit_token = []
    unit_token = []

    valid_units = u.keys()
    length = len(dur_str)
    first_char = dur_str[0]
    if (not first_char.isdigit()) and (not first_char in ["-", "+", "."]):
        raise DurationParseError("Invalid duration string")

    for i, character in enumerate(dur_str):
        last_char = i == (length - 1)
        # safe peek for logging only
        next_char = dur_str[i + 1] if (i + 1) < length else None

        if character.isdigit():
            if unit_token:
                unit_token, duration_token, duration_tokens = flush_unit_token(unit_token, valid_units, duration_token, duration_tokens)
            digit_token.append(character)
            continue


        if character in ["-", "+", "."]:
            if last_char:
                raise DurationParseError(f'Invalid unit: {"".join(unit_token) + character}')
            if unit_token:
                if not dur_str[i + 1].isdigit():
                    
                    unit_token.append(character)
                    continue
                else:
                    unit_token, duration_token, duration_tokens = flush_unit_token(unit_token, valid_units, duration_token, duration_tokens)
                digit_token.append(character)
            else:
                digit_token.append(character)
            continue


        if not character.isdigit():
            if digit_token:
                
                float_token = "".join(digit_token)

                try:
                    float_token = float(float_token)
                except:
                    raise DurationParseError(f"Invalid number: {float_token}")

                duration_token.append(float_token)
                digit_token = []

            if character != " ":
                unit_token.append(character)

            if last_char:
                unit_token, duration_token, duration_tokens = flush_unit_token(unit_token, valid_units, duration_token, duration_tokens)

    return duration_tokens

print(scan(test))
