#!/usr/bin/python3
"""get status with request"""

import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    res = r.text
    print("Body response:")
    print("\t - type: {}".format(type(res)))
    print("\t - content: {}".format(res))
