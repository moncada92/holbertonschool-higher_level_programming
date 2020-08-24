#!/usr/bin/python3
"""post request urllib"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as req:
        print(req.read().decode('utf-8'))
