#!/usr/bin/python3

import sys


def main():
    lst = sys.argv[1:]
    total = 0
    if len(lst) >= 0:
        for i in lst:
            try:
                total += int(i)
            except Exception as e:
                print("an error has occured {}".format(e))
    print(total)


if __name__ == "__main__":
    main()
