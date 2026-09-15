#!/usr/bin/env python3
"""Module that prints and returns the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of number (always positive) and return it."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit))
    return last_digit
