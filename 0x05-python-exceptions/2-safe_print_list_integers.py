#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            len += 1
        except (ValueError, TypeError):
            continue
        i += 1
    return len
