#!/usr/bin/python3
"""
This module contains a function to print the statistics of a text file.
"""


def print_stats(file):
    """
    This function prints the statistics of a text file.

    Args:
        file (str): The name of the file to analyze.
    """
    lines = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    file_size = 0

    with open(file, "r") as f:
        for line in f:
            lines += 1
            split_line = line.split()
            try:
                status_code = split_line[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except IndexError:
                pass
            try:
                file_size += int(split_line[-1])
            except (ValueError, IndexError):
                pass

    print("File size: {:d} bytes".format(file_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{:s}: {:d}".format(code, count))
