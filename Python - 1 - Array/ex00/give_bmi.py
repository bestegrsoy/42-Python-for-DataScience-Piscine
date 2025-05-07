def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate BMI values based on height and weight.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must be\
                              of the same length.")

        for h in height:
            if not isinstance(h, (int, float)):
                raise TypeError("All height values must be int or float.")

        for w in weight:
            if not isinstance(w, (int, float)):
                raise TypeError("All weight values must be int or float.")

        bmi_list = []
        for h, w in zip(height, weight):
            bmi = w / (h ** 2)
            bmi_list.append(bmi)
        return bmi_list

    except Exception as e:
        print(f"Error: {e}")


def apply_limit(bmi_list: list[int | float], limit: int) -> list[bool]:
    """
    Determines whether the BMI value is higher or
    lower than the limit and returns true or false.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans indicating whether
        each BMI value is above the limit.
    """
    if not all(isinstance(b, (int, float)) for b in bmi_list):
        raise TypeError("All BMI values must be int or float.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    return [b > limit for b in bmi_list]
