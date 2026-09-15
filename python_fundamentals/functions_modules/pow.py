#!/usr/bin/env python3
"""Module that raises a number to a power without using **."""


def pow(a, b):
    """Return a raised to the power of b, computed manually with a loop."""
    result = 1
    for _ in range(b):
        result *= a
    return result
