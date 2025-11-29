#!/usr/bin/python3
'"This is writing the file'''


def write_file(filename='', text=''):
    '''This is wiriting thw text to the file and returns the count'''

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
