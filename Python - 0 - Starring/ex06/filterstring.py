from ft_filter import ft_filter
import sys


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer
    Strings do not contain any special characters.
    (Punctuation or invisible)
    Returns a list of words that are longer than the integer.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s = sys.argv[1]
        n = sys.argv[2]

        if not n.isdigit():
            raise AssertionError("the arguments are bad")

        n = int(n)

        if not all(c.isalpha() or c.isspace() for c in s):
            raise AssertionError("the arguments are bad")

        result = list(ft_filter(lambda word: len(word) > n, s.split()))

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
