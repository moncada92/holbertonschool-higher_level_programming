#!/usr/bin/python3
""" POST in API with requests """

import requests
import sys

if __name__ == "__main__":
    json = {'q': ""}
    if len(sys.argv) > 1:
        json['q'] = sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", json)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if response.json():
            print("[{}] {}".format(response.json().get('id'),
                  response.json().get('name')))
        else:
            print("No result")
