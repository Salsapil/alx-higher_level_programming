#!/usr/bin/python3
"""module"""


def is_same_class(obj, a_class):
    """is same class:
    checks if the object is exactly an instance of the specified class"""
    return type(obj) is a_class
