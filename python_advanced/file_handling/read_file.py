#!/usr/bin/env python3
"""Define a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Print the content of a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        # end="" keeps the file content exactly as it is (no extra newline)
        print(f.read(), end="")
