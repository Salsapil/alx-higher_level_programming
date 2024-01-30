#!/usr/bin/python3
def magic_string():
    magic_string.current = getattr(magic_string, 'current', 0) + 1
    return "BestSchool, " * (magic_string.current - 1) + "BestSchool"
