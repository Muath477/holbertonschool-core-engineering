#!/usr/bin/env python3
"""Demonstrate inheritance and polymorphism with Animal subclasses."""


class Animal:
    """Represent a generic animal."""

    def speak(self):
        """Return the sound made by the animal."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog, a type of Animal."""

    def speak(self):
        """Return the sound made by a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat, a type of Animal."""

    def speak(self):
        """Return the sound made by a cat."""
        return "Meow"


if __name__ == "__main__":
    for animal in (Animal(), Dog(), Cat()):
        print(animal.speak())

    dog = Dog()
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
    print(isinstance(dog, Cat))
