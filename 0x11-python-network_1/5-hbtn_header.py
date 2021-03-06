#!/usr/bin/python3
""" get X-Request-Id with Requests """

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('x-request-id'))
