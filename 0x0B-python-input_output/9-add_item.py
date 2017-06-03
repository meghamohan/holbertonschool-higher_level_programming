#!/usr/bin/python3
""" script that adds all arguments to a Python list,
 and then save them to a file """


import sys
import os
loadFromFile = __import__('8-load_from_json_file').load_from_json_file
saveToFile = __import__('7-save_to_json_file').save_to_json_file
fileName = "add_item.json"

if __name__ == "__main__":
    if os.path.exists(fileName):
        try:
            list1 = loadFromFile(fileName)
        except:
            list1 = []
    else:
        list1 = []
    for arg in range(1, len(sys.argv)):
        list1.append(sys.argv[arg])
    saveToFile(list1, fileName)
