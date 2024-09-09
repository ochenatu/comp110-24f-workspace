"""Tea Party Exercise - EX01"""

__author__ = "730766896"


"""Main function to execute all functions when called"""


def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for", guests, "People!")  # Amount of people
    print("Teabags: ", tea_bags(people=guests))  # Amount of tea bags
    print("Treats: ", treats(people=guests))  # Amount of treats
    print(
        "Cost: ${}".format(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # Total Cost
    return None


"""When called will get how many people want tea and return int"""


def tea_bags(people: int) -> int:
    return people * 2
    # 2 tea bags for each person


"""Computes the number of treats needed based on the number of teas guests are expecting to drink"""


def treats(people: int) -> int:
    return int(tea_bags(people=people) * 1.5)
    # For each 2 tea bags, a person will want 1.5 treats, also convert to int


"""Compute the cost of the tea bags and the treats combined,"""


def cost(tea_count: int, treat_count: int) -> float:
    tea_cost = tea_count * 0.5
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost  # total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
