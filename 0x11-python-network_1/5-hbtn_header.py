#!/usr/bin/python3
"""

"""
import requests
import sys


if __name__ == "__main__":
    reqst = requests.get(sys.argv[1])
    print(reqst.headers.get('X-Request-Id'))
