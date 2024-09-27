#!/usr/bin/python3
"""
This function reads a text file (UTF8) and prints it to stdout
"""

def read_file(filename=""):
    """
    Reads the content of a specified file and prints it to the standard output.

    This function opens a file in read mode with UTF-8 encoding, reads its content, 
    and prints it without adding an extra newline at the end. If the file does not exist 
    or cannot be opened, an error will be raised.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If the file cannot be opened.
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
