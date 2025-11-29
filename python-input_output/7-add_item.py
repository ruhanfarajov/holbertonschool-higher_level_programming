#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-loadd-from_json_file').load_from_json_file

'''this is doing america great again by helping the mission'''


def add_item():
    '''This is adding items to the list of jsj'''
    filename = 'add_item.js'
    if Path(filename).exists():
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ = "__main__":
    add_item()
