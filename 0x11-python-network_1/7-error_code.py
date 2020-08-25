#!/usr/bin/env python3
""" get statud code with requests """

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if int(r.status_code) >= 400:
        print(r.status_code)
    else:
        print(r.text)
