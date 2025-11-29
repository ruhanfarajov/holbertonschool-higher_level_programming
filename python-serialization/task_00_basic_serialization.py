#!/usr/bin/python3
'''This is just a file for serialization and deserialization'''
import json


def serialize_and_save_to_file(data, filename):
    '''This has got methods to write a file'''
    if not isinstance(data, dict):
        raise TypeError("the data must be dictonary!")
    with open(filename, 'w', encoding='utf-8')as file:
        file.write(json.dumps(data))


def load_and_deserialize(filename):
    '''this is returning the file content as dict'''

    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
