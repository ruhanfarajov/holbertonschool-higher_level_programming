#!/usr/bin/python3
'''Making America Great Again by doing TRUMP's missions'''


class BaseGeometry():
    '''Making America Great Again by doing TRUMP's missions'''
    def area(self):
        '''raises and exception mesaage that area is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
