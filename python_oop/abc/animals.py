#!/usr/bin/env python3
"""Define an abstract Animal class and its concrete subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent a generic animal with an abstract sound behavior."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
