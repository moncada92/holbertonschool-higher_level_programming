#!/usr/bin/python3
""" POST in API with requests """

import requests
import sys

if __name__ == "__main__":

    payload = {'q': ""}

    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]

    r = requests.get("http://0.0.0.0:5000/search_user", data=payload)
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if r.json():
            res = r.json()
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
