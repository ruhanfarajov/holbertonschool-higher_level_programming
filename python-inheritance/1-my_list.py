#!/usr/bin/python3
"""Module that defines MyList class which can print itself sorted."""


class MyList():
    """Class that extends list with ability to print sorted version."""

    def __init__(self, data=[]):
        """Prints the list in ascending sorted order."""
        self.data = list(data)

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print("{}".format(sorted(self.data)))

    def append(self, value):
        '''appends the list a value'''
        self.data.append(value)

    def __repr__(self):
        '''return my _list'''
        return repr(self.data)
