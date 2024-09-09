"""My first CQ in COMP110!"""

__author__ = "730766896"


def mimic(message: str) -> str:
    """Takes input and repeats it back to you"""
    return message


def main() -> None:
    """Main function to call mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
