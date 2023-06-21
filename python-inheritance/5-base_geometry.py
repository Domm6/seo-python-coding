#!/usr/bin/python3
"""
This class is for geometry
"""


class BaseGeometry:
    """
    A base class representing geometry.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: When called, as the area() method\
            is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
