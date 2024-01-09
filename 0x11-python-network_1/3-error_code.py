#!/usr/bin/python3
"""
take in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
handle error
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    url = sys.argv[1]
    requ = request.Request(url)
    try:
        with request.urlopen(requ) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
