#!/usr/bin/python3
"""

"""
import requests
import sys


if __name__ == "__main__":
    params = {'email': sys.argv[2]}
    reqst = requests.post(sys.argv[1], data=params)
    print(reqst.text)
