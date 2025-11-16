#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str(number)[-1]
if int(s) > 5:
    print(f"Last digit of {number} is {s} and is greater than 5")
elif int(s) == 0:
    print(f"Last digit of {number} is {s} and 0")
elif int(s) < 6:
    print(f"Last digit of {number} is {s} and is less than 6 and not 0")
