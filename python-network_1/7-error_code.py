#!/usr/bin/python3
'''
Script that takes a URL as a command-line argument, sends a GET request,
and displays the response body or an error code if the status is >= 400.
'''
import requests
import sys


def fetch_and_display(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display(url)
