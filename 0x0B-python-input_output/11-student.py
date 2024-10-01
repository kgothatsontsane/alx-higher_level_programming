#!/usr/bin/python3
"""
This module defines the Student class, which is used to 
represent a student with attributes for first name, last name,
and age. 

It also includes methods for initializing a student object and
converting it to a JSON-serializable dictionary.
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

    def to_json(self, attrs=None):
        """
        The function `to_json` converts object attributes to a dictionary,
        optionally filtering based on specified attributes.

        Args:
            attrs (list): A list of attributes to include in the JSON
            representation.If `None`, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes of
            the object. If `attrs` is `None`, all attributes are included.
        """
        if attrs is None:
            return self.__dict__
        else:
            return ({key: self.__dict__[key] for key
                    in attrs if key in self.__dict__})

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values
        from the provided dictionary.

        Args:
            json (dict): A dictionary containing the new values for the
            attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
