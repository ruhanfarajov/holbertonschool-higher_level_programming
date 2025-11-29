#!/usr/bi/python3
'''Let's learn how to pickle vaooo'''
import pickle


class CustomObject():
    '''This is a custom class for students'''

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''this is just printing out everything'''
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        ''' Using pickle to serialize the item'''
        with open(filename, 'wb') as file:
            try:
                file.write(pickle.dumps(self))
            except Exception as e:
                print("An error occured: {}".format(e))

    @classmethod
    def deserialize(cls, filename):
        '''This is deserializing the element'''
        try:
            with open(filename, "rb") as file:
                return pickle.loads(file.read())
        except Exception as e:
            print("An error occured: {}".format(e))
            return None
