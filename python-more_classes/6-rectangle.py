#!/usr/bin/python3
"This defines a rectangle with witdh and height"


class Rectangle:
    "this add methods to this class"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        "Let's set some variables"
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        "this is width getter"
        return self.__width

    @property
    def height(self):
        "this is height getter"
        return self.__height

    @width.setter
    def width(self, value):
        "the property setter for width"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        "this is property setter for the height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        "this is returning the perimeter"
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def area(self):
        "this is returning the area"
        return (self.__height * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        "Returns a string representation of the rectangle for recreation"
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
