#!/usr/bin/python3
"""
    Base Geometry class based on 4-base_geometry class. Has the area method
    that raises an exception if the area methods isn't used. The class\
    method that validates integers.
"""


class BaseGeometry:
    """ Based on the empty base geometry class and 4-base_geometry. """

    def area(self):
        """ Public instance method  of the area, raises\
        exception if the area isn't used. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function that validates the value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
