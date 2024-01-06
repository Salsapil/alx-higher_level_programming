#!/usr/bin/python3
def element_at(my_list, idx):
    lenn = len(my_list)
    if idx < 0 or idx > lenn:
        return None
    else:
        return my_list[idx]
