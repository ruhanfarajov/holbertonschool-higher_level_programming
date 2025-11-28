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

    def __repr__(self):
        '''Returns self string kadksdjl'''
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
    
    def area(self):
        "calculate area of the given cell"
        return self.__width * self.__height
