#!/usr/bin/python3
"""module for inheritance"""


class MyList(list):
    """class MyList inherits from list"""
    def print_sorted(self):
        """print_sorted:
            prints the list, but sorted"""
        print(sorted(self))
