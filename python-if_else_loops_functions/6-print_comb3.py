#!/usr/bin/python3
for i in range(0, 100):
    if i == 89:
        print("{:2d}".format(i))
    else:
        for j in range(i+1, 100):
            if str(i) == str(j)[::-1] or "0" + str(i) == str(j)[::-1]:
                print("{:02d}".format(i), end=", ")
