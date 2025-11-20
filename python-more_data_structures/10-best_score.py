#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    lst = list(a_dictionary)
    if len(lst) == 0:
        return None
    best = lst[0]
    for i in lst:
        if a_dictionary[i] > a_dictionary[best]:
            best = i
    return best
