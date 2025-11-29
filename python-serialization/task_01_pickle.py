#!/usr/bi/python3
'''Let's learn how to pickle vaooo'''
import pickle


class CustomObject():
    '''This is a custom class for students'''

    def __init__(self, name, age, is_student):
        self.__name = name
        self.__age = age
        self.__is_student = is_student

    def display(self):
        '''this is just printing out everything'''
        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))
        print("Is Student: {}".format(self.__is_student))

    def serialize(self, filename):
        ''' Using pickle to serialize the item'''
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(F.pickle.dump(self.__dict__))

    @classmethod
    def deserialize(cls, filename):
        '''This is deserializing the element'''

        with open(filename, 'r', encoding='utf-8') as file:
            return pickle.load(file.read())
