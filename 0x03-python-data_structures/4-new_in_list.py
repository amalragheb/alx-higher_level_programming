#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    count = len(my_list) - 1
    if idx < 0 or idx > count:
        return my_list
    if idx <= count:
        new[idx] = element
    return new
