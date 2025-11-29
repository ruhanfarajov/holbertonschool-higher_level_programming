#!/usr/bin/python3
'''This is just a file for serialization and deserialization'''
import json


def serialize_and_save_to_file(data, filename):
    '''This has got methods to write a file'''
    with open(filename, 'w', encoding='utf-8')as file:
        try:
                file.write(json.dumps(data))
            except Exception as e:
                print("Input Error: {}".format(e))

def load_and_deserialize(filename):
    '''this is returning the file content as dict'''

    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
