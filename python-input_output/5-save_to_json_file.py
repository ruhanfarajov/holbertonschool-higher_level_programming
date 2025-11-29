#!/usr/bin/python3
'"This is writing the file'''
import json


def save_to_json_file(my_obj, filename):
    '''This is wiriting thw text to the file and returns the count'''

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
