#!/usr/bin/python3
"""

"""
import urllib.request
import sys


if __name__ == "__main__":
    reqst = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reqst) as response:
        #  print(response.headers)-> to list all headers
        print(response.getheader('X-Request-Id'))
