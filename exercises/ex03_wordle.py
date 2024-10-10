"""Wordle Exercise - EX02"""

__author__ = "730766896"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """Ask for a guess and then check if it is the length of the secret word"""
    guess = input("Enter a {} character word: ".format(secret_word_len))
    # Loop if not correct length
    while len(guess) != secret_word_len:
        guess = input("That wasn't {} chars! Try again: ".format(secret_word_len))

    # Final check for length
    if len(guess) == secret_word_len:
        return guess
    else:
        return ""


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searches for occurences of char_guess in secret_word"""
    i = 0
    assert len(char_guess) == 1
    # Check if secret_word contains char_guess for each index, returning True if it does
    while i < len(secret_word):
        if char_guess == secret_word[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Turns each letter of guess in their corresponding emojis relating to secret"""
    assert len(guess) == len(secret)
    i = 0
    emoji = ""
    # Checks which type each character is
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        i += 1
    return emoji


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    limit = 6
    # Run main process of the game
    while turn <= limit:
        print("=== Turn {}/6 ===".format(turn))
        guess = input_guess(len(secret))
        if guess == secret:
            print(emojified(guess, secret))
            print("You won in {}/6 turns!".format(turn))
            return None
        else:
            print(emojified(guess, secret))
        turn += 1
    # If runs out of turns, print game over message
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
        return None


# Call main
if __name__ == "__main__":
    main(secret="codes")
