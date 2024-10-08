#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


class Student(object):
    """
    A class used to represent a Student.

    Attributes:
    ----------
    first_name : str
        The first name of the student.
    last_name : str
        The last name of the student.
    age : int
        The age of the student.

    Methods:
    -------
    __init__(self, first_name, last_name, age):
        Initializes the Student with first name, last name, and age.

    to_json(self):
        Returns the dictionary description with simple data structure
        for JSON serialization of an object.
    """

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
