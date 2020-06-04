#!/usr/bin/env python3

"""
module for def load_from_json_file(filename)
"""

import sys
import os.path
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


objt = sys.argv[1:]

list_n = []

if os.path.exists("./add_item.json"):
    list_n = load_from_json_file("add_item.json")

save_to_json_file(list_n + objt, "add_item.json")
