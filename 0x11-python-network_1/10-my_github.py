#!/usr/bin/python3
""" get id in github API """

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(user, password))

    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        print(res.get('id'))
