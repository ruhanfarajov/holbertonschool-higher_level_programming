#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    lst = list(a_dictionary)
    if len(lst) == 0:
        return a_dictionary
    else:
        new_dict={}
        for i in lst:
            new_dict[i] = a_dictionary[i] * 2
        return new_dict
