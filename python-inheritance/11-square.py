#!/usr/bin/python3
'"Importing the functions inside 9-rectangle  to create a square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''THIS IS THE CLASS FOR INITIALIZING A SQUARE'''

    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def __repr__(self):
        "this is doing the great job"
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
