#!/usr/bin/python3
"""module for inheritance"""


class MyList(list):
    """class MyList inherits from list"""
    def print_sorted(self):
        """print_sorted:
            prints the list, but sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
