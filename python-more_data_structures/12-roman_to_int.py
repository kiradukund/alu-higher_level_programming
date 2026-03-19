#!/usr/bin/python3
"""Module that converts a Roman numeral string to an integer."""


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer. Returns 0 if invalid input."""
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev = 0

    for char in reversed(roman_string):
        current = roman_values.get(char, 0)
        if current < prev:
            result -= current
        else:
            result += current
        prev = current

    return result
