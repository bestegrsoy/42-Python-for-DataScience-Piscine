class calculator:
    """
    A calculator class for performing arithmetic operations on vectors.

    This class enables element-wise addition, multiplication, subtraction,
    and division of a vector with a scalar value.
    """
    def __init__(self, vector):
        """
        Initialize the calculator with a vector.

        Args:
            vector: A list or array-like object containing numeric values.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Element-wise addition of the vector with a scalar.

        Args:
            object: A scalar value to add to each element of the vector.

        Returns:
            None: Prints the resulting vector after addition.
        """
        value = [x + object for x in self.vector]
        print(value)

    def __mul__(self, object) -> None:
        """
        Element-wise multiplication of the vector with a scalar.

        Args:
            object: A scalar value to multiply with each element of the vector.

        Returns:
            None: Prints the resulting vector after multiplication.
        """
        value = [x * object for x in self.vector]
        print(value)

    def __sub__(self, object) -> None:
        """
        Element-wise subtraction of a scalar from the vector.

        Args:
            object: A scalar value to subtract from each element of the vector.

        Returns:
            None: Prints the resulting vector after subtraction.
        """
        value = [x - object for x in self.vector]
        print(value)

    def __truediv__(self, object) -> None:
        """
        Element-wise division of the vector by a scalar.

        Args:
            object: A scalar value to divide each element of the vector by.

        Returns:
            None: Prints the resulting vector after division.

        Raises:
            ZeroDivisionError: If the division is attempted by zero.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero.")
            result = [x / object for x in self.vector]
            print(result)
        except Exception as e:
            print(f"Error: {e}")
