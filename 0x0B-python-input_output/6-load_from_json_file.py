#!/usr/bin/python3
"""
This module contains a function that creates an Object from a “JSON file”.
"""


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        object: The Python object created from the JSON file.
    """
    import json

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
