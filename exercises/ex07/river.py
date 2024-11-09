"""File to define River class."""

__author__ = "730766896"

from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check the ages of fish and bears"""
        current_bears = list(self.bears)
        current_fish = list(self.fish)
        # Check fish > 3
        for f in range(0, len(current_fish)):
            if current_fish[f].age > 3:
                current_fish.pop(f)
        # Check bears > 3
        for f in range(0, len(current_bears)):
            if current_bears[f].age > 5:
                current_bears.pop(f)
        self.bears = current_bears
        self.fish = current_fish
        return None

    def bears_eating(self):
        """Model bears eating"""
        for f in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
            f.eat(3)
        return None

    def check_hunger(self):
        """Check if bear dies from hunger"""
        current_bears = list(self.bears)
        for f in range(0, len(current_bears)):
            if current_bears[f].hunger_score < 0:
                current_bears.pop(f)
        self.bears = current_bears
        return None

    def repopulate_fish(self):
        """Repopulates fish"""
        if len(self.fish) >= 2:
            if len(self.fish) // 2 == 0:
                offspring: int = int((len(self.fish) / 2) * 4)
            else:
                offspring: int = int(((len(self.fish) - 1) / 2) * 4)
            for _ in range(0, offspring):
                self.fish.append(Fish())

        return None

    def repopulate_bears(self):
        """Repopulates bears"""
        if len(self.bears) >= 2:
            if len(self.bears) // 2 == 0:
                offspring: int = int(len(self.bears) / 2)
            else:
                offspring: int = int((len(self.bears) - 1) / 2)
            for _ in range(0, offspring):
                self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints status of river"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week by calling days"""
        i = 0
        while i != 7:
            self.one_river_day()
            i += 1

    def remove_fish(self, amount: int) -> None:
        """Removes fish from river"""
        current_fish = list(self.fish)
        for f in range(0, amount):
            current_fish.pop(f)
        self.fish = current_fish
