#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set(my_list)
    sum = 0
    for i in x:
        sum += i
    return sum


# my_list = [1, 2, 3, 1, 4, 2, 53]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))
