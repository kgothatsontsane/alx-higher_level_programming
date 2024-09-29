#!/usr/bin/python3
"""
This function appends a string at the end of a text file (UTF8) and
returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the
    number of characters added.
    """

    with open(filename, "a", encoding='utf-8') as file:
        file.write(text)
        return count_characters(text)


def count_characters(text):
    """
    Return the number of characters in a string.
    """
    return len(text)
