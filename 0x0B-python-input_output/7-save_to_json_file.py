#!/usr/bin/python3
import json
""" function that writes an Object to a text file,
 using a JSON representation """


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file1:
        file1.write(json.dumps(my_obj))
