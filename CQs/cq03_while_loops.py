"""While Loops CQ03"""

__author__ = "730766896"


def num_instances(phrase: str, search_char: str) -> int:
    """Finds how many of instances character is in a phrase"""
    count = 0
    index = 0
    # Loop for indexing and comparing
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1
    return count


if __name__ == "__main__":
    """Main function to call num_instanes"""
    print(num_instances("heeeeeeloooo", "o"))
