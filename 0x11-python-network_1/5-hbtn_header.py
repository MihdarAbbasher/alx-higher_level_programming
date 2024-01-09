#!/usr/bin/python3
"""
 takes in a URL arg, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':

    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
