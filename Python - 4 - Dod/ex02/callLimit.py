def callLimit(limit):
    """
    Creates a decorator that limits the number of times
    a function can be called.

    Parameters:
        limit (int): Maximum number of allowed function calls

    Returns:
        function: A decorator that restricts the wrapped
                 function to 'limit' calls,
                 printing an error message on excess calls

    Example:
        @callLimit(3)
        def test_function():
            print("Function called")

        # Will work for the first 3 calls, then print an error
    """
    count = {"val": 0}

    def callLimiter(function):
        """
        Wraps the target function with call counting functionality.

        Parameters:
            function: The function to be limited

        Returns:
            function: The wrapped function with call limiting
        """
        def limit_function(*args, **kwds):
            """
            Executes the original function if under
            call limit, otherwise prints error.

            Parameters:
                *args: Positional arguments passed to the original function
                **kwds: Keyword arguments passed to the original function

            Returns:
                The result of the original function if under call limit,
                None otherwise
            """
            if count["val"] < limit:
                count["val"] += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function

    return callLimiter
