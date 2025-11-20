#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    lst = list(a_dictionary)
    for i in lst:
        a_dictionary[i] *= 2
    return a_dictionary
