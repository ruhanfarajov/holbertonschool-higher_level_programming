#!/usr/bin/python3

def uppercase(str):
    s = ""
    for i in str:
        if ord(i) >= 97 and ord("i") <= 122:
            ch_add = ord(i) - 32
            s += chr(ch_add)
        else:
            s += i
    print("{}".format(s))
