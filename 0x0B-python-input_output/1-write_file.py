#!/usr/bin/python3
"""
This function writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.

    This function opens a file in write mode with UTF-8 encoding,
    writes the provided text to the file, and returns
    the number of characters written. If the file does not exist,
    it will be created. If the file already exists,
    its content will be overwritten.

    Args:
        filename (str): The path to the file to be written to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
