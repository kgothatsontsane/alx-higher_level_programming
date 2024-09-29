#!/usr/bin/python3
"""
This module contains a function that returns
an object (Python data structure)
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    This function uses the json module to parse a JSON string and convert it
    back to the corresponding Python data structure.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python data structure represented by the JSON string.

    Examples:
        >>> from_json_string('[1, 2, 3]')
        [1, 2, 3]
        >>> from_json_string('{"id": 12, "name": "John"}')
        {'id': 12, 'name': 'John'}
    """
    import json

    return json.loads(my_str)
