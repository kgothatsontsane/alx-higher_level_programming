#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: A dictionary containing all attributes of the obj class.
    """
    return obj.__dict__
