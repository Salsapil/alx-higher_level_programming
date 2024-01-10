#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    # will be key with max value. If negative, function will return None.
    max_key = None
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
