#!/usr/bin/python3
"""

"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/user'
    try:
        req = requests.get(url, auth=(user, pswd))
        print(req.json()['id'])
    except:
        print("None")
