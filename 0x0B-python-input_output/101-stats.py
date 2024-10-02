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
    with open(file, "r") as f:
        lines = f.readlines()
        print(f"{len(lines)} lines")
        for line in lines:
            words = line.split()
            print(f"{len(words)} words")
            for word in words:
                print(f"{len(word)}: {word}")
        f.close()
