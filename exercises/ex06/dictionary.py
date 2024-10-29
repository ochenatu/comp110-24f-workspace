"""Dictionary Ex06"""

__author__ = "730766896"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert key and values in dictionary"""
    y = 0  # Counter
    for elem in x:
        for i in x:
            if elem == i:
                y += 1
    if y > 1:
        raise KeyError("Keys must be unique!")
    copy = {}
    for elem in x:
        copy[x[elem]] = elem
    return copy


def favorite_color(x: dict[str, str]) -> str:
    """Find highest count of color in dict"""
    y = 0  # Counter
    z = 0  # Max value
    fav = ""
    for elem in x:
        for i in x:
            if x[elem] == x[i]:
                y += 1
        if y > z:
            z = y
            fav = x[elem]
    return fav


def count(x: list[str]) -> dict[str, int]:
    """Create a dictionary with unique key and count of how many times in list"""
    y: dict[str, int] = {}
    for elem in x:
        if elem not in y:
            y[elem] = x.count(elem)
    return y


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Organize str values based on letter"""
    y = {}
    for elem in x:
        first_letter = elem[
            0
        ].lower()  # Take out the first letter and convert  to lowercase
        if first_letter not in elem:
            y[first_letter] = []  # Make a new list if the letter not in dictionary
        y[first_letter].append(elem)  # Add word to list for letter
    return y


def update_attendance(x: dict[str, list[str]], day: str, student: str) -> None:
    """Add student to specific attendance date"""
    for elem in x:
        if day == elem:
            x[elem].append(student)
