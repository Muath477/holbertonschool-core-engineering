#!/usr/bin/env python3
"""Module that prints a string in uppercase."""


def uppercase(str):
    """Print str in uppercase (ASCII conversion), followed by a newline."""
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
print("{}".format(result))
