#!/usr/bin/python3

def uniq_add(my_list=[]):
    lst = set(my_list)
    total = 0
    for i in lst:
        total += i
    return total
