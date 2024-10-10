"""CQ04 Coordinates"""

__author__ = "730766896"


def get_coords(xs: str, ys: str) -> None:
    "Creates coordinates of each index of each two strings using double while loop"
    i = 0
    j = 0
    while i < len(xs):
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
        j = 0
