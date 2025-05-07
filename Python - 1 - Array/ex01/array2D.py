def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (matrix) from row `start` to `end`,
    prints the shape before and after slicing.

    Args:
        family (list): A 2D list (list of lists) representing the matrix.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing (not inclusive).

    Returns:
        list: A new 2D list containing the sliced rows.

    Raises:
        TypeError: If `family` is not a list of lists, or
        if `start` or `end` is not an integer.
        ValueError: If rows in the matrix are not all the same length.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("Family must be a list of lists")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("Family must be a list of lists")

        row_lenght = len(family[0])
        if not all(len(row) == row_lenght for row in family):
            raise ValueError("All rows must be of the same length")

        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end must be integer")

        print(f"My shape is : ({len(family)}, {len(family[0])})")
        sliced = family[start:end]
        rows = len(sliced)
        cols = len(sliced[0]) if sliced else 0
        print(f"My new shape is : ({rows}, {cols})")

        return sliced

    except Exception as e:
        print(f"Error: {e}")
