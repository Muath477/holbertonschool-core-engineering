#!/usr/bin/env python3
"""Print only the integers among the first x elements of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the integers among the first x elements and return how many."""
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            # not an integer, skip it. IndexError is deliberately not caught,
            # so asking for more elements than the list has still raises.
            pass
    print()
    return printed
