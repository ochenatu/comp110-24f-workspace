"""Dictionary Ex06"""

__author__ = "730766896"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert key and values in dictionary"""
    inverted: dict[str, str] = {}
    for key, elem in x.items():
        if elem in inverted:
            raise KeyError("Duplicate found")
        inverted[elem] = key
    return inverted


def favorite_color(x: dict[str, str]) -> str:
    """Find highest count of color in dict"""
    if x == {}:
        return ""
    count: dict[str, int] = {}
    for color in x.values():
        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    fav: str = ""
    max_count: int = 0
    for color, y in count.items():
        if y > max_count:
            max_count = y
            fav = color

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
    y: dict[str, list[str]] = {}
    for elem in x:
        first_letter = elem[0].lower()  # Take out the first letter and convert
        if first_letter not in y:
            y[first_letter] = []  # Make a new list if the letter not in dictionary
        y[first_letter].append(elem)  # Add word to list for letter
    return y


def update_attendance(x: dict[str, list[str]], day: str, student: str) -> None:
    """Add student to specific attendance date"""
    if day not in x:
        x[day] = []

    if student not in x[day]:
        x[day].append(student)
