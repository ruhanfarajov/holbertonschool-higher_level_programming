#!/usr/bin/python3

class MyList():

    def __init__(self, data=[]):
        self.data = list(data)

    def print_sorted(self):
        self.data.sort()

    def append(self, value):
        self.data.append(value)

    def __repr__(self):
        return repr(self.data)
