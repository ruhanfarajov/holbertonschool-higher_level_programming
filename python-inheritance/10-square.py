#!/usr/bin/python3
'"Importing the functions inside 9-rectangle  to create a square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''THIS IS THE CLASS FOR INITIALIZING A SQUARE'''

    def __init__(self, size):
        self = Rectangle.__init__(self, size, size)
