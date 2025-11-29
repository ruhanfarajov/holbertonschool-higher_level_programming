#!/usr/bin/python3
'''THIS IS CREATING STRING FORMATED DATA FROM JSON'''
import json


def from_json_string(my_str):
    '''This is the main converter function'''
    return json.loads(my_str)
