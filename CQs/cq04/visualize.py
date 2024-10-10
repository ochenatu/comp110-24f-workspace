"""CQ04 Visualize"""

__author__ = "730766896"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x = "123"
y = "abc"

if __name__ == "__main__":
    "Main function"
    print(concat(x, y))
    get_coords(x, y)
