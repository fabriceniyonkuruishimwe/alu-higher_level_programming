#!/usr/bin/python3
"""Module that defines a function to convert a class instance to a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class with simple serializable attributes
            (list, dict, string, integer, boolean).

    Returns:
        dict: a dictionary representation of obj's instance attributes.
    """
    return obj.__dict__
