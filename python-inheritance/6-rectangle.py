#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry
"""

class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Initializes the Rectangle class """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """ Returns a string representation of the Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Calculates the area of the Rectangle """
        return self.__width * self.__height
