import sys


def text_to_morse(text):
    """
    Converts a given text to Morse code.
    Only letters (a-z, A-Z), digits (0-9) and space are allowed.
    Space is represented as '/' in Morse.

    Args:
        text (str): The input text to convert.

    Returns:
        str: Morse code translation.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input contains unsupported characters.
    """

    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',
        'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }

    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    text = text.upper()
    morse_code = []

    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            raise AssertionError("the arguments are bad")

    return ' '.join(morse_code)


def main():
    """
    Main function that handles command-line arguments
    and prints the Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Only one argument is required.")

        input_text = sys.argv[1]
        morse_code = text_to_morse(input_text)
        print(morse_code)

    except AssertionError as ae:
        print(f"AssertionError: {ae}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
