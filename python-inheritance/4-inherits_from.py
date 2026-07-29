#!/usr/bin/python3
"""Module that defines a function to check if obj is inherited from a_class."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a class that inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
