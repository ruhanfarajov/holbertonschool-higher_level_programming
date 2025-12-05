#!/usr/bin/python3
'''
I am doing well
'''

import requests
import sys


def fetch(url):
    custom = {'cfclearance': 'true'}
    html = requests.get(url, headers=custom)
    body = html.headers
    result = body.get('X-Request-Id')
    print(result)


if __name__ == "__main__":
    try:
        lst = sys.argv
        url = lst[1]
        fetch(url)
    except Exception as e:
        print("Error happened: {}".format(e))
