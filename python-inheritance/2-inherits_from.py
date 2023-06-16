#!/usr/bin/python3
"""
Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
    """
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class is not a_class
