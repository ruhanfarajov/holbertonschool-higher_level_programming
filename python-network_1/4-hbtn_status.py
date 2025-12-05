#!/usr/bin/python3
'''
I am doing well
'''

import requests

def fetch(url):
    html = requests.get(url)
    body = html.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    fetch(url)
