from .units import UNITS as u
from .exceptions import DurationParseError

test = "hr30min15secs"

def scan(dur_str):

    duration_tokens = []
    duration_token = []
    digit_token = []
    unit_token = []

    length = len(dur_str)
    for i, character in enumerate(dur_str):
        last_char = i == (length - 1)
        
        if character.isdigit():
            if unit_token:
                duration_token.append(unit_token)
                duration_tokens.append(duration_token)
                unit_token = []
                duration_token = []
            digit_token.append(character)
            counter += 1
            continue
        if not character.isdigit():
            if digit_token:
                duration_token.append(digit_token)
                digit_token = []
            if character != " ":
                unit_token.append(character)

            if last_char:
                duration_token.append(unit_token)
                duration_tokens.append(duration_token)

    return duration_tokens

print(scan(test))
