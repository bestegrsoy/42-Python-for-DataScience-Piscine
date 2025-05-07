from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistical measures on a set of numeric values.

    This function computes statistical operations specified in kwargs
    on the numeric values provided in args.

    Parameters:
        *args: Variable length argument list of numbers (int or float)
              These are the values to perform statistical operations on.
              If no args are provided, "ERROR" will be printed for each kwarg.

        **kwargs: Variable length keyword arguments where:
                 - keys can be any string
                 - values must be one of: "mean", "median",
                   "quartile", "std", "var"
                   to specify which statistical operation to perform

    Operations:
        - mean: Calculates the arithmetic mean (average) of the values
        - median: Finds the middle value of the sorted data
        - quartile: Returns a list with first (25%) and third (75%) quartiles
        - std: Calculates the standard deviation (population)
        - var: Calculates the variance (population)

    Returns:
        None: Results are printed to stdout
    """
    if len(args) == 0:
        for _ in range(len(kwargs)):
            print("ERROR")
        return

    try:
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("All arguments must be integers or floats")

        sorted_arg = sorted(args)

        for key, operation in kwargs.items():
            if operation == "mean":
                value = sum(sorted_arg) / len(sorted_arg)
                print(f"mean : {value}")

            elif operation == "median":
                n = len(sorted_arg)
                if n % 2 == 0:
                    median = (sorted_arg[n // 2 - 1] + sorted_arg[n // 2]) / 2
                else:
                    median = sorted_arg[n//2]
                print(f"median : {median}")

            elif operation == "quartile":
                n = len(sorted_arg)
                q1_index = n // 4
                q3_index = (n * 3) // 4
                quartiles = [float(sorted_arg[q1_index]),
                             float(sorted_arg[q3_index])]
                print(f"quartile : {quartiles}")

            elif operation == "std":
                mean = sum(args) / len(args)
                variance = sum((x - mean) ** 2 for x in args) / len(args)
                std_dev = variance ** 0.5
                print(f"std : {std_dev}")

            elif operation == "var":
                mean = sum(args) / len(args)
                variance = sum((x - mean) ** 2 for x in args) / len(args)
                print(f"var : {variance}")

    except Exception:
        print("ERROR")


if __name__ == '__main__':
    ft_statistics()
