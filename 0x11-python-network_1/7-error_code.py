#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
 and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    reqst = requests.get(sys.argv[1])
    if reqst.status_code >= 400:
        print("Error code:", reqst.status_code)
    else:
        print(reqst.text)
