#!/usr/bin/python3
"""Divide two numbers and always report the result."""


def safe_print_division(a, b):
    """Return a / b (or None if it fails) and always print the result."""
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        # finally runs whether or not the division raised
        print("Inside result: {}".format(result))
    return result
