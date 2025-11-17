#!/usr/bin/python3

import sys


def main():
    lst = sys.argv[1:]
    if len(lst) == 1:
        print("{} argument:".format(len(lst)))
    else:
        print("{} arguments:".format(len(lst)))
    for i in range(0, len(lst)):
        print("{}: {}".format(i+1, lst[i]))


if __name__ == "__main__":
    main()
