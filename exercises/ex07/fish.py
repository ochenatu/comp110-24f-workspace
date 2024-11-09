"""File to define Fish class."""

__author__ = "730766896"


class Fish:

    age: int

    def __init__(self):
        """Initializes object"""
        self.age = 0
        return None

    def one_day(self):
        """Adds one day to age"""
        self.age += 1
        return None
