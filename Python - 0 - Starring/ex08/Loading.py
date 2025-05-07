import sys
from time import sleep


def ft_tqdm(lst: range) -> None:
    """
    Takes an iterable and displays a progress bar like tqdm.

    Args:
    lst (Iterable): Iterable data to loop over

    Yields:
    iterable elements are looped through in order

    """
    try:
        if not hasattr(lst, '__iter__'):
            raise TypeError("Error: Only iterable objects")

        total = len(lst)
        if total == 0:
            raise ValueError("Error: An empty iterable cannot be sent")

        for i, item in enumerate(lst):
            percent = (i + 1) / total
            bar_length = 123
            filled_lenght = int(bar_length * percent)
            bar = '=' * filled_lenght + '>' + ' ' * \
                (bar_length - filled_lenght - 1)
            sys.stdout.write(f"\r{int(percent * 100)}%|"
                             f"[{bar}] {i + 1} / {total}")
            sys.stdout.flush()
            yield item

        print()

    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


def main():
    for elem in ft_tqdm(range(100)):
        sleep(0.01)


if __name__ == "__main__":
    main()
