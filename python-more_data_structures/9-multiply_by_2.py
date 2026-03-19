#!/usr/bin/python3
"""Module that returns a new dictionary with all values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values doubled."""
    return {key: value * 2 for key, value in a_dictionary.items()}
