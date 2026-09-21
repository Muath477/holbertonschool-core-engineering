#!/usr/bin/env python3
"""Print a value only if it is an integer."""


def safe_print_integer(value):
    """Print value as an integer and return True, otherwise return False."""
    try:
        # "{:d}" raises ValueError for str/float and TypeError for None/list
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
