"""Finding the max"""

__author__ = "730766896"


def find_and_remove_max(vals: list[int]) -> int:
    """Find max and remove, return max"""
    saved_max = 0
    first_check = 0

    if len(vals) == 0:
        return -1

    # Finds max value
    for elem in range(0, len(vals), 1):
        if first_check == 0:
            saved_max = vals[elem]
            first_check += 1
        else:
            if vals[elem] >= saved_max:
                saved_max = vals[elem]

    # Removes all cases of max value
    vals[:] = [x for x in vals if x != saved_max]

    return saved_max
