#!/usr/bin/python3
"""

"""
import sys
import requests


if __name__ == "__main__":
    lettr = ""
    if len(sys.argv) > 1:
        lettr = sys.argv[1]
    param = {'q': lettr}
    reqst = requests.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        jsonParam = reqst.json()
    except:
        print("Not a valid JSON")
        sys.exit()
    if jsonParam:
        print("[{}] {}".format(jsonParam.get('id'), jsonParam.get('name')))
    else:
        print("No result")
