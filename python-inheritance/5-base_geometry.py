#!/usr/bin/python3
"""
This module defines the Square class that represents a square.
"""


class BaseGeometry:
    """
    A base class representing geometry.

    This class serves as a foundation for defining geometric shapes and operations.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: When called, as the area() method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
