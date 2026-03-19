#!/usr/bin/python3
"""Module that multiplies all values in a list using map."""


def multiply_list_map(my_list=[], number=0):
    """Returns a new list with all values multiplied by number."""
    return list(map(lambda x: x * number, my_list))
