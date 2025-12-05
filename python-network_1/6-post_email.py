#!/usr/bin/python3
'''
this is making america great again
'''

import sys
import requests


def fetch(url, email):
    payload = {'email': email}
    headers_ = {'cfclearance': 'true'}

    response = requests.post(url, data=payload, headers=headers_)
    body = response.text
    print(body)


if __name__ == "__main__":
    lst = sys.argv
    fetch(lst[1], lst[2])
