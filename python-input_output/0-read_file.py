#!/usr/bin/python3
'''THIS IS A FUNCTION READING THE FILE AND PRINTING IT'''


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
