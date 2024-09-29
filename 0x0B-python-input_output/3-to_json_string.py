#!/usr/bin/python3
"""
This module contains a function that returns the
JSON representation of an object.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    This function uses the json module to convert an object to its JSON
    representation. The object can be of any type, but it must be a
    serializable object.

    Args:
        my_obj (object): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.

    Examples:
        >>> to_json_string([1, 2, 3])
        '[1, 2, 3]'
        >>> to_json_string({ 'id': 12, 'name': "John" })
        '{"id": 12, "name": "John"}'
    """
    import json

    return json.dumps(my_obj)
