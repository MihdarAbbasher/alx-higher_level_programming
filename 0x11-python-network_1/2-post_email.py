#!/usr/bin/python3
"""
 a Python script that:
takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    url = sys.argv[1]

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        response = res.read()
        print(response.decode('utf-8'))
