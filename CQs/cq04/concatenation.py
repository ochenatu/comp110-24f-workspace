"""CQ04 Concatenation"""

__author__ = "730766896"

word1 = "happy"
word2 = "tuesday"


def concat(istr: str, jstr: str) -> str:
    "Combines both strings and returns"
    return str(istr) + str(jstr)


if __name__ == "__main__":
    "Make sure it isnt called from visualize.py"
    print(concat(word1, word2))
