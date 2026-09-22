#!/usr/bin/env python3
"""Define shape interfaces and demonstrate duck typing."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Represent a generic shape interface."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a new Circle.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print the area and perimeter of any shape-like object.

    Relies purely on duck typing: any object exposing area() and
    perimeter() methods works here, regardless of its actual type.

    Args:
        obj: An object exposing area() and perimeter() methods.
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
