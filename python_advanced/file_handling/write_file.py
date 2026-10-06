#!/usr/bin/env python3
"""Define a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, overwriting its content.

    The file is created if it does not exist.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
