#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.print_sorted([1, 5, 9], 1)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
