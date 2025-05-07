def square(x: int | float) -> int | float:
    """Return the square of x."""
    return (x * x)


def pow(x: int | float) -> int | float:
    """Return x to the power of x."""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Return a function that will apply function to x n times."""
    count = [x]

    def inner() -> float:
        count[0] = function(count[0])
        return count[0]

    return inner
