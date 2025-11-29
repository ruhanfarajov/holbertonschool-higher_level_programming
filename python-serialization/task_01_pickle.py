#!/usr/bi/python3
'''Let's learn how to pickle vaooo'''


class CustomObject():
    '''This is a custom class for students'''

    def __init__(self, name, age, is_student):
        self.__name = name
        self.__age = age
        self.__is_student = is_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name should be a string!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age should be an integer!")
        self.__age = value

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_student should be boolean")
        self.__is_student = value

    def display(self):
        '''this is just printing out everything'''
        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))
        print("Is Student: {}".format(self.__is_student))

    def serialize(self, filename):
        ''' Using pickle to serialize the item'''
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(pickle.dumps(self.__dict__))

    @classmethod
    def deserialize(cls, filename):
        '''This is deserializing the element'''

        with open(filename, 'r', encoding='utf-8') as file:
            return pickle.loads(file.read())
