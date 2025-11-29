#!/usr/bin/python3
'"This is writing the file'''
import json


def load_from_json_file(filename):
    '''This is wiriting thw text to the file and returns the count'''

    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
