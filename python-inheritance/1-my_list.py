#!/usr/bin/python3
'''Making America Great Again'''


class MyList():
    '''I am not working'''

    def __init__(self, data=[]):
        '''initialize the variable'''
        self.data = list(data)

    def print_sorted(self):
        '''sort the list'''
        self.data.sort()

    def append(self, value):
        '''appends the list a value'''
        self.data.append(value)

    def __repr__(self):
        '''return my _list'''
        return repr(self.data)
