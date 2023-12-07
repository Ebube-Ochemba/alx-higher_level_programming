#!/usr/bin/python3

"""7-add_item
This script adds all arguments to a python list and
save them into a specific given file
"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)

except:
    new_list = []

for arguments in argv[1:]:
    new_list.append(arguments)

save_to_json_file(new_list, filename)
