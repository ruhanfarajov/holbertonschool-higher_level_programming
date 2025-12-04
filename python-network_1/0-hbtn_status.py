#!/usr/bin/python3

#!/usr/bin/python3
"""
0-hbtn_status.py

Fetches the URL https://intranet.hbtn.io/status using urllib,
then displays"""


import urllib.request

def fetch_status(url):
    """
    Fetch the given URL and return the raw response body (bytes).
    """
    with urllib.request.urlopen(url) as response:
        return response.read()

def main():
    url = "https://intranet.hbtn.io/status"
    body = fetch_status(url)

    # Print result in required format
    print("Body response:")
    print(" - type: {}".format(type(body)))
    print(" - content: {}".format(body))
    try:
        text = body.decode('utf-8')
    except Exception:
        text = body.decode('utf-8', errors='replace')
    print("    - utf8 content: {}".format(text))

if __name__ == "__main__":
    main()
