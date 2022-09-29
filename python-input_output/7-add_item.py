#!/usr/bin/python3

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    ''' if file exists it will open the file using the previous done function,
    and load the already existed list into the "list_from_json" list '''
    list_from_json = load_from_json_file(filename)
except FileNotFoundError:
    ''' if the file doesn't exist (along with the list suppodes inside),
    it will create the list anyway'''
    list_from_json = []
''' it doesn't matter if it exisits or not the file, it will upgrade the list
with the new arguments passed, and save it with using the function'''
save_to_json_file(list_from_json + argv[1:], filename)
