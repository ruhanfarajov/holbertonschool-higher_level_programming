#!/usr/bin/python3
'"This is writing the file and MAGA'''


def append_write(filename='', text=''):
    '''This is wiriting thw text to the file and returns the count'''

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
