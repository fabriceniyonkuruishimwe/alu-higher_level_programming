#!/usr/bin/python3
"""Module that defines a class BaseGeometry with integer validator."""


class BaseGeometry:
    """A class BaseGeometry."""

    def area(self):
        """Raise an Exception with message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
