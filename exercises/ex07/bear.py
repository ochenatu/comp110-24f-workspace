"""File to define Bear class."""

__author__ = "730766896"


class Bear:

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes object"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Adds one day to age"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Changes hunger"""
        self.hunger_score += num_fish
