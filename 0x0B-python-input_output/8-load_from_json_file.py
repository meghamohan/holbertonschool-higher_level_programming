#!/usr/bin/python3
import json
""" function that creates an Object from a JSON file """


def load_from_json_file(filename):
    with open(filename, 'r') as myObj:
        return json.loads(myObj.read())
