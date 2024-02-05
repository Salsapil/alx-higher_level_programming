#!/usr/bin/python3
"""module"""


def inherits_from(obj, a_class):
    """is same class:
    checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""
    return isinstance(obj, a_class) and type(obj) != a_class
