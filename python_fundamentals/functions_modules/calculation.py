#!/usr/bin/env python3
"""Program that imports arithmetic functions and prints their results."""
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = 10
    b = 5
    add_line = "Add: {} + {} = {}".format(a, b, add(a, b))
    sub_line = "Sub: {} - {} = {}".format(a, b, sub(a, b))
    mul_line = "Mul: {} * {} = {}".format(a, b, mul(a, b))
    div_line = "Div: {} / {} = {}".format(a, b, div(a, b))
    print(add_line + "\n" + sub_line + "\n" + mul_line + "\n" + div_line)
