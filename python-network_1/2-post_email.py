#!/usr/bin/python3
'''
I am doing everything
'''
import urllib.request
import urllib.parse
import sys


def post(url, email):
    data = {"email": email}
    encoded = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, encoded)
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        body = response.read()
        body = body.decode('utf-8')
        print(body)


if __name__ == "__main__":
    try:
        lst = sys.argv[1:]
        post(lst[0], lst[1])
    except Exception as e:
        print("Error: {}".format(e))
