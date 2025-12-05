#!/usr/bin/python3
'''
This is doing pythoning here
'''

import urllib.request
import sys


def fetch(url):
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        fetch(url)
    except Exception as e:
        print("Error: {}".format(e))
