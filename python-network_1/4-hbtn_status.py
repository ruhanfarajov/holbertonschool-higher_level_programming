#!/usr/bin/python3
'''
I am doing well
'''

import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        body = html.decode('utf-8')
        print(type(body))
        print(body)


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    fetch(url)
