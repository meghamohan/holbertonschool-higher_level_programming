#!/usr/bin/python3
import json
""" function that returns an object (Python data structure)
 represented by a JSON string """


def to_json_string(my_obj):
    return json.dumps(my_obj)
