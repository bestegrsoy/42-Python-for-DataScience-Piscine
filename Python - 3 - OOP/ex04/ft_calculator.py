class calculator:
    """
    A simple calculator class that operates on vectors.
    All methods are static and don't require an instance.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints the dot product of two vectors."""
        result = sum(float(x) * float(y) for x, y in zip(V1, V2))
        print(f"Dot product is: {int(result)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the element-wise addition of two vectors."""
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints the element-wise subtraction of two vectors."""
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
