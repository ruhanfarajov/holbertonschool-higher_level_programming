#!/usr/bin/python3
'''
this file is urrllib requesting
'''

import sys
import urllib.request
import urllib.error
import urllib.parse


def error_code(url):
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        body = body.decode('utf-8')
        print(body)


if __name__ == "__main__":
    try:
        lst = sys.argv
        error_code(lst[1])
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print("Error code: {}".format(e.code))
        elif hasattr(e, 'reason'):
            print("Error reason: {}".format(e.reason))
    except Exception as e:
        print("{}".format(e))
