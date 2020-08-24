#!/usr/bin/python3
"""display X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as res:
        value = res.headers.get('X-Request-Id')
        print (value)
