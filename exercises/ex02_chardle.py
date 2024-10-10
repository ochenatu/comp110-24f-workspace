"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730766896"


def input_word() -> str:
    """Asks for a 5 character word and checks length"""
    word = input("Enter a 5-character word:")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Asks for a 1 character word and checks length"""
    letter = input("Enter a single character:")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Counts occurences of letter in word"""
    i = 0
    instance = 0
    print("Searching for " + letter + " in " + word)
    # Check if word contains letter for each index, returning True if it does
    while i < len(word):
        if letter == word[i]:
            print(letter + " found at index " + str(i))
            instance += 1
        i += 1
    # Grammar check
    if instance == 1:
        print(str(instance) + " instance of " + letter + " found in " + word)
    elif instance > 1:
        print(str(instance) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """Main functions to ask other functions"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
