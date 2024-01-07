#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter(q)>
If no letter is provided, sends `q=""`.
"""

if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    mydata = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=mydata)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
