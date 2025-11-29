#!/usr/bin/python3
'"This is writing the file'''


def append_write(filename='', text=''):
    '''This is wiriting thw text to the file and returns the count'''

    with open(filename, 'a', encoding='utf-8') as file:
        file.append(text)
    return len(text)
