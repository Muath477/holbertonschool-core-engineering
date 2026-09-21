#!/usr/bin/env python3
"""Print the first x elements of a list without crashing."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list and return how many were printed."""
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:
        # x was bigger than the list: stop and report what was printed
        pass
    print()
    return printed
