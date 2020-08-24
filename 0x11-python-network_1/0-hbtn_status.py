#!/usr/bin/python3
""" get resquest with urllib"""

import urllib.request

if __name__ == "__main__":

    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        read = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(read)))
        print("\t- content: {}".format(read))
        print("\t- utf8 content: {}".format(read.decode('utf-8')))
