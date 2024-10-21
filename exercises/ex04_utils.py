"""Utils Exercise"""

__author__ = "730766896"


def all(x: list[int], y: int) -> bool:
    """Compares values in list to a given integer"""
    for elem in x:
        if elem != y:
            return False
    if len(x) == 0:
        return False
    return True


def max(x: list[int]) -> int:
    """Checks each value of list and finds which is max"""
    max: int = 0
    # Error Check
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    # Actual function to check for max
    for elem in range(0, len(x), 1):
        if elem == 0:
            max = x[elem]
        else:
            if x[elem] > max:
                max = x[elem]
    return max


def is_equal(x: list[int], y: list[int]) -> bool:
    """Compares values in list to a another list"""
    # Checks length to avoid out of bounds error
    if len(x) != len(y):
        return False
    # Compares each index of both functions if same length
    for elem in range(0, len(x), 1):
        if x[elem] != y[elem]:
            return False
    return True


def extend(x: list[int], y: list[int]) -> None:
    """Appends second list to end of first list"""
    for elem in y:
        x.append(elem)
