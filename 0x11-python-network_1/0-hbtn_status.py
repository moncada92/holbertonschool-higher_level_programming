#!/usr/bin/env python3
""" get resquest with urllib"""
import urllib.request
import ssl

if __name__ == "__main__":
    context = ssl._create_unverified_context()
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req, context=context) as res:
        read = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(read)))
        print("\t- content: {}".format(read))
        print("\t- utf8 content: {}".format(read.decode('utf-8')))
