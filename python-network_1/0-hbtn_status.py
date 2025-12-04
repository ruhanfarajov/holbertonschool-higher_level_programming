#!/usr/bin/python3
'''this is importing so good things'''
import urllib.request


def fetch(url):
    '''fethcing the document'''
    req = urlib.request.Request(
            url,
            headers={"cfclearance: "true}
    )

    with urlib.request.urlopen(req) as response:
        return response.read(-).decode('utf-8')

if __name__ == "__main__":
    '''safer way'''
    print(fetch('https://intranet.hbtn.io/status'))
