"""Utils Program"""

__author__ = "730766896"


def only_evens(x: list[int]) -> list[int]:
    """Create a list with only the even numbers of x list"""
    y: list[int] = []
    for elem in x:
        if elem % 2 == 0:
            y.append(elem)
    return y


def sub(x: list[int], num1: int, num2: int) -> list[int]:
    """Create a list of the numbers in the given range"""
    y: list[int] = []
    for elem in range(num1, num2 + 1, 1):
        y.append(x[elem])
    return y


def add_at_index(x: list[int], num1: int, num2: int) -> None:
    """Inserts num1 at index of num2 in x list"""
    if num2 < 0 or num2 > len(x):
        raise IndexError("Index is out of bounds for the input list")
    x.insert(num1, num2)
