#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(len(my_list))):
        print(my_list[i])

# def print_reversed_list_integer(my_list=[]):
#     lenn = len(my_list)
#     for i in range(lenn):
#         lenn = lenn - 1
#         print("{:d}".format(my_list[lenn]))
