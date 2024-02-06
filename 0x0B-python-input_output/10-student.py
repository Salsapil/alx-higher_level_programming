#!/usr/bin/python3
"""module"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for attr in attrs:
                if not isinstance(attr, str):
                    return self.__dict__
        except Exception:
            return self.__dict__
        dict_new = dict()
        for i, j in self.__dict__.items():
            if i in attrs:
                dict_new[i] = j
        return dict_new
