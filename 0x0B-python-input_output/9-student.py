#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


class Student(object):
    """docstring for Student."""

    first_name = str()
    last_name = str()
    age = int()

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary description with simple data structure
        for JSON serialization of an object.

        Args:
            obj (object): An instance of a class.

        Returns:
            dict: A dictionary containing all attributes of the obj class.
        """
        return self.__dict__
