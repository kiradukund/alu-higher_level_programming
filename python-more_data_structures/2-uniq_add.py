#!/usr/bin/python3
"""Module that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """Returns sum of all unique integers in the list."""
    return sum(set(my_list))
