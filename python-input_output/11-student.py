#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of the Student instance.

        Args:
            attrs (list): optional list of attribute names to include.
                If not a list of strings, all attributes are returned.

        Returns:
            dict: a dictionary representation of this instance's attributes,
                filtered by attrs if provided.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): a dictionary of attribute names and values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
