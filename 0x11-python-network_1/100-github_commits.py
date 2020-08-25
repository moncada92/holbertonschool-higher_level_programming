#!/usr/bin/python3
""" get id in github API """

import requests
import sys

if __name__ == "__main__":
    i = 0
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo_name, owner)
    r = requests.get(url)

    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        for data in res:
            if i > 9:
                break
            print(data.get('sha') + ': ', end="")
            print(data.get('commit').get('author').get('name'))
            i += 1
