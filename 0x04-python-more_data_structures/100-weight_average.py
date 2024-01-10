#!/usr/bin/python3
def weight_average(my_list):
    if my_list is None:
        return 0
    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for score, weight in my_list)
    weighted_average = numerator / denominator
    return weighted_average
