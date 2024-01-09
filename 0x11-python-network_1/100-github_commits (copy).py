#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for commit in commits:
            print (commit)
            print("\n---------\n\n")
    except IndexError:
        pass
