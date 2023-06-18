#!/usr/bin/python3
"""
This class serves as a foundation for defining geometric shapes and operations.
"""


class BaseGeometry:
    """
    A base class representing geometry.
    """
    def area(self):
        """
        Calculate the area of the geometric shape.
        """
        raise Exception("area() is not implemented")
    """
    Validate the value as an integer.
        
    """
    def integer_validator(self, name, value):
        """
        Validate the value as an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        """
        Validate the value as an integer.
        """
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
