#!/usr/bin/python3
'''
SALAM THIS MODULE CAN BE DOCUMENTD AS SCRIPT

'''


class Student():
    '''This is a student class created by user'''

    def __init__(self, first_name, last_name, age):
        '''initializing variables here'''
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
    except Exception as e:
        print("{}".format(e))

    def to_json(self):
        '''
        this just return json formatted data
        '''
        return self.__dict__
