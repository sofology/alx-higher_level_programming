#!/usr/bin/python3

"""module 7-add_item"""


import sys
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

new_list = []

try:
    new_list = list(load_from_json_file('add_item.json'))
except:
    len(new_list) is 0

for a in range(1, len(sys.argv)):
    new_list.append(sys.argv[a])
save_to_json_file(new_list, "add_item.json")
