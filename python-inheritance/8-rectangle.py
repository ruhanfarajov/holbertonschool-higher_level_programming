#!/usr/bin/python3
'''Making America Great Again by doing TRUMP's missions'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Making America Great Again by doing TRUMP's missions'''

    def __init__(self, width, height):
        '''Making America Great Again by doing TRUMP's missions'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
