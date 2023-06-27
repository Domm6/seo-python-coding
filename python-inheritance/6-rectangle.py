#!/usr/bin/python3
"""
Rectangle class that inherits from BaseGeometry
"""
import BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Initializes the Rectangle class """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """ Returns a string representation of the Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
