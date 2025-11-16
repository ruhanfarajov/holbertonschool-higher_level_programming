#!/usr/bin/python3
file = open("text", "r")
for line in file:
    print(line, end="")
file.close()
