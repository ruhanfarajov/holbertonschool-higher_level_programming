#!/usr/bin/python3
'''
I am doing well
'''

import requests
import sys


def fetch(url):
    html = requests.get(url)
    body = html.headers
    print(body)


if __name__ == "__main__":
    try:
        lst = sys.argv
        url = lst[1]
        fetch(url)
    except Exception as e:
        print("Error happened: {}".format(e))
