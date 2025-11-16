#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{:2d}".format(i))
    else:
        for j in range(i, 100):
            if str(i) == str(j)[::-1]:
                print("{:02d}".format(i), end=", ")
