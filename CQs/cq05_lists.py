"""Mutating functions."""

__author__ = "730766896"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], b: int) -> None:
    """Adds number to list"""
    a.append(b)


def double(a: list[int]) -> None:
    """Doubles each index"""
    i = 0
    while i < len(a):
        a[i] = a[i] * 2
        i += 1


if __name__ == "__main__":
    """Main function"""
    double(list_2)
    print(list_1)
    print(list_2)
