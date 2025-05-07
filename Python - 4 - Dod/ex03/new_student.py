import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Creating random str for id with random function.
    k=15 determines how many characters we want for the random ID.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student with automatically generated login and ID.

    Attributes:
        name (str): Student's first name
        surname (str): Student's last name
        active (bool): Whether the student is active, defaults to True
        login (str): Auto-generated from first initial and surname
        id (str): Auto-generated unique identifier

    Example:
        >>> student = Student("John", "Doe")
        >>> student.login  # Returns "JDoe"
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname}"
        self.id = generate_id()
