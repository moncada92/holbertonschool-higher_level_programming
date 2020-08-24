#!/usr/bin/env python3
"""display X-Request-Id"""
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request("https://intranet.hbtn.io/status")

    with urllib.request.urlopen(req) as res:
        value = res.headers.get('X-Request-Id')
        print (value)
