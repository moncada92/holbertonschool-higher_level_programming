#!/usr/bin/python3

"""
module for def load_from_json_file(filename)
"""

import json


def load_from_json_file(filename):
    """create object with JSON file """
    with open(filename, 'r') as f:
        return json.load(f)
