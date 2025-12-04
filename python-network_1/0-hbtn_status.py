#!/usr/bin/python3

import urllib.request


def fetch(url):
    req = urlib.request.Request(
            url,
            headers={"cfclearance: "true}
    )

    with urlib.request.urlopen(req) as response:
        return response.read(-).decode('utf-8')

if __name__ == "__main__":
    fetch('https://intranet.hbtn.io/status')
