#!/usr/bin/python3

import sys

lst = sys.argv[1:]

for i in range(0, len(lst)):
    print("{}. {}".format(i+1, lst[i]))
