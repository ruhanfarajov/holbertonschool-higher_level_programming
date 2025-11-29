#!/usr/bin/python3
'''
SALAM THIS MODULE CAN BE DOCUMENTD AS SCRIPT
'''


class Student():
    '''This is a student class created by user'''

    def __init__(self, first_name, last_name, age):
        '''initializing variables here'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, my_list=None):
        '''
        this just return json formatted data
        '''
        dict_ = {}
        if my_list is None:
            return self.__dict__
        elif len(my_list) == 0:
            return dict_
        for i in my_list:
            for j in self.__dict__:
                if i == j:
                    dict_[i] = self.__dict__[j]
        return dict_
