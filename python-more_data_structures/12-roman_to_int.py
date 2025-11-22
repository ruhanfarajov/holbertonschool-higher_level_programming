#!/usr/bin/python3

def roman_to_int(roman_string):
    lst = ['I', 'IV', 'V', 'IX', 'X', 'L', 'C', 'D', 'M']
    lst2 = [1, 4, 5, 9, 10, 50, 100, 500, 1000]
    total = 0
    if not isinstance(roman_string, str):
        return total
    i = 0
    while i < len(roman_string):
        if roman_string[i] not in lst:
            return 0
        for j in range(0, len(lst)):
            if roman_string[i:i+2] == lst[j]:
                total += lst2[j]
                i += 2
                break
            elif roman_string[i] == lst[j]:
                total += lst2[j]
                i += 1
    return total
