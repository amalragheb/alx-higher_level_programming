#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = len(my_list) - 1
    if idx < 0 or idx > count:
        return my_list
    if idx <= count:
        my_list[idx] = element
    return my_list
