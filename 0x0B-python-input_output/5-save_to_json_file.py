#!/usr/bin/python3
"""module"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    with open(filename, "w", encoding="UTF8") as file:
        json.dump(my_obj, file)
