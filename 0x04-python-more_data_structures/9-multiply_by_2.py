#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    # Iterate over the key-value pairs
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
