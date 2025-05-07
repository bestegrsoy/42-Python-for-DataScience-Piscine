import sys


def count_func(text):
    """
    Counts and displays the number of total characters,
    upper and lower case letters, digits, punctuation marks,
    and spaces in the text.
    """
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    full_count = len(text)
    upper_count = sum(1 for x in text if x.isupper())
    lower_count = sum(1 for x in text if x.islower())
    punctuation_count = sum(1 for x in text if x in punctuation_characters)
    space_count = sum(1 for x in text if x == " ")
    digit_count = sum(1 for x in text if x.isdigit())

    print(f"The text contains {full_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main(ac, av):
    """
    Main function to handle input and call count_func.
    If argument is passed via CLI(Command line interface), it uses that.
    Otherwise reads from stdin.
    """
    try:
        if ac == 1:
            count_func(av)
        elif ac == 0:
            print("What is the text to count?")
            av = sys.stdin.read()
            if not av.strip():
                raise ValueError("No input provided.")
            count_func(av)
        else:
            raise ValueError("Too many arguments provided.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ac = len(sys.argv) - 1
    av = sys.argv[1] if ac > 0 else None
    main(ac, av)
