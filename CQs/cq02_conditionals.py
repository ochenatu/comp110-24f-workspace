"""Conditionals CQ02"""

__author__ = "730766896"


def guess_a_number() -> None:
    """Has a secret number, and asks for a number, and compares it to secret"""
    secret: int = 7
    num: int = int(input("Guess a number:"))
    print("Your guess was {}".format(num))
    # Choices
    if num == secret:
        print("You got it!")
    elif num < secret:
        print("Your guess was too low! The secret number is {}".format(secret))
    elif num > secret:
        print("Your guess was too high! The secret number is {}".format(secret))


if __name__ == "__main__":
    """Main function to call guesser"""
    guess_a_number()
