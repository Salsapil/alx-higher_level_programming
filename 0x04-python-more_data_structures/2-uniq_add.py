#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set()
    for int in my_list:
        if int not in uniq_set:
            uniq_set.add(int)  # set use add
    return sum(uniq_set)
