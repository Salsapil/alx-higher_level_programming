#!/usr/bin/python3
"""
module:
This is the third task
in Test-Driven-Development
"""


def say_my_name(first_name, last_name=""):
    """function
    Args:
        first_name: First Name
        last_name: Last Name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
